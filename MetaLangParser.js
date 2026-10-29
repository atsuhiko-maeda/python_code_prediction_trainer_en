// 仕様：
// - textNodeに近いほうのタグから反映される：self-closingは左から右，open/closeは内側から外側
// - includeBlock, select，optionは一階層のみ．それ以外のタグは入れ子可
// - meta[replace]:等の:はなくてもよい（レガシー仕様）．なるべくミスを減らす仕様に変更．
// - 値としての]は\でエスケープ入力可．
// - ’や”は逆の引用符で入力可．
// - xmlと同じく&apos;等も可
// - 属性値に配列[“a”,’b’]を入力可(XMLと異なる)

// （参考）XMLの仕様：　
// - <>&”’は参照でエスケープ（一方，この言語は<>はそのまま属性値として入力可）．
// - 属性値は”や’で必ず囲む必要あり．"'"や'"'として，引用符も入力可．あるいは参照でエスケープする
// - エスケープ対象: < > & ” ’  ---> &lt; &gt; &amp; &quot; &apos;
// - 属性値としての配列表記はない．慣習的には”a,b,c”．

class MetaLangParser {
    // HTMLコメント内のmetaコマンドを検索（開始タグと終了タグの両方に対応）
    // /[ \t]*(?:\/\/|\/\*|#|<!--)[ \t]* ← 行頭スペース・タブ,コメント記号 (// /* # <!--)
    // <(\/?meta\[[^\]]*\] ← <タグ開始, (キャプチャ開始，\/?閉じタグ，
    // (?:[^>"']|"[^"]*"|'[^']*')*?)>  ← >"'以外 or " "で囲まれた, ''で囲まれた以外，>で終わる
    static htmlCommentPattern = /[ \t]*(?:\/\/|\/\*|#|<!--)?[ \t]*<(\/?meta\[[^\]]*\](?:[^>"']|"[^"]*"|'[^']*')*?)>/g;
    static closeTagPattern = /^\/meta\[([^\]]+)\]/;
    static openTagPattern = /^meta\[([^\]]+)\](?::?\s*(.*))?/;
    //属性値："a",'a',[...]に対応(xmlでは[...]は不可)
    static attrPattern = /(\w+)\s*=\s*(?:"((?:[^"\\]|\\.)*)"|'((?:[^'\\]|\\.)*)'|\[((?:[^\]\\]|\\.)*)\])/g;
    //["a","b"]や['a','b']用．JSON.parse()は["a","b"]しか使えないので使用しない
    static listPattern = /(?:"((?:[^"\\]|\\.)*)"|'((?:[^'\\]|\\.)*)')/g;


    constructor() {
        this.metaCommands = [];

        this.current_pos = 0;
        this.ctx = [];
        this.errors = [];

        this.result = [];
    }

    /**
     * HTMLファイルの内容をパースしてメタ言語コマンドを抽出
     * @param {string} htmlContent - HTMLファイルの内容
     * @returns {Object} パース結果
     */
    parse(htmlContent) {
        this.metaCommands = [];
        this.errors = [];

        this.current_pos = 0;

        try {
            // メタコマンドを抽出
            this.extractMetaComments(htmlContent);
            // 構造を解析してネスト関係を構築
            this.buildNestStructure();

            console.log(this.printStructure());
            return {
                success: true,
                metaCommands: this.metaCommands,
                errors: this.errors
            };
        } catch (error) {
            this.errors.push(`Parse error: ${error.message}`);
            return {
                success: false,
                metaCommands: this.metaCommands,
                errors: this.errors
            };
        }
    }

    /**
     * HTMLコメント内のメタコマンドを抽出
     */
    extractMetaComments(content) {
        console.log("=========== extractMetaComments() ===========");
        let match;
        MetaLangParser.htmlCommentPattern.lastIndex = 0;
        // MetaLangParser.htmlCommentPattern2.lastIndex = 0;
        
        for (const match of content.matchAll(MetaLangParser.htmlCommentPattern)) {

            let text = content.substring(this.current_pos, match.index);
            // text = text.replace(MetaLangParser.htmlCommentPattern2, '');
            console.log("textNode:"+text.replaceAll("\n","\\n"));
            if (text!==""){
                this.metaCommands.push({
                    type:"textNode",
                    command: "textNode",
                    attributes: {},
                    raw: text
                });
            }

            // const command = this.parseMetaCommand((match[1] || match[2]).trim(), match.index);
            const command = this.parseMetaCommand(match[1].trim(), match.index);

            if (command) {
                // console.log("tag: "+JSON.stringify(command));
                this.metaCommands.push(command);
                if (command.type!=="self-closing"){
                    const s = content.indexOf("\n",match.index + match[0].length);
                    this.current_pos = s>0 ? s+1 : match.index + match[0].length;//改行+1 から次を走査
                }
                else
                    this.current_pos = match.index + match[0].length;
            }
        }

        // const text = content.substring(this.current_pos,content.length).replace(MetaLangParser.htmlCommentPattern2, '');
        const text = content.substring(this.current_pos,content.length);
        // console.log("textNode:"+text.replaceAll("\n","\\n"));
        if (text!==""){
            this.metaCommands.push({
                type:"textNode",
                command: "textNode",
                raw: text
            });
        }
    }

    /**
     * メタコマンドをパースして構造化されたオブジェクトに変換
     */
    parseMetaCommand(commandText, position) {
        try {
            // 自己完結型かクローズタグかを判定
            const isSelfClosing = commandText.endsWith('/');
            const isCloseTag = commandText.startsWith('/meta[');

            if (isCloseTag) {
                // クローズタグの処理
                
                const closeMatch = commandText.match(MetaLangParser.closeTagPattern);
                if (closeMatch) {
                    return {
                        type: 'close',
                        command: closeMatch[1],
                        raw: commandText
                    };
                }
            } else {
                // 開始タグまたは自己完結タグの処理
                const openMatch = commandText.match(MetaLangParser.openTagPattern);//:はなくてもよい仕様に変更
                if (openMatch) {
                    const command = openMatch[1].replace('/', ''); // 自己完結型の/を除去
                    const attributesPart = openMatch[2] || '';
                    const attributes = this.parseAttributes(attributesPart);

                    return {
                        type: isSelfClosing ? 'self-closing' : 'open',
                        command: command,
                        attributes: attributes,
                        raw: commandText
                    };
                }
            }

            this.errors.push(`Failed to parse command: ${commandText}`);
            return null;
        } catch (error) {
            this.errors.push(`Error parsing command "${commandText}": ${error.message}`);
            return null;
        }
    }

    /**
     * 属性文字列をパースしてオブジェクトに変換
     */
    parseAttributes(attributeString) {
        if (!attributeString.trim()) return {};

        const attributes = {};
        
        // 属性のパターンをマッチング
        MetaLangParser.attrPattern.lastIndex = 0;

        let match;

        while ((match = MetaLangParser.attrPattern.exec(attributeString)) !== null) {
            const key = match[1];            
            //""は，JSではfalsy，よって
            //"" || undefined はundefinedになる．一方，??だと左辺がnull/undefinedのときだけ右辺を評価
            let value = match[2] ?? match[3] ?? match[4] ;

            // 配列形式の値を処理
            if (match[4]) {
                try {
                    let inner_match;
                    MetaLangParser.listPattern.lastIndex = 0;
                    let tmp_list = [];
                    while ((inner_match = MetaLangParser.listPattern.exec(match[4])) !== null) {
                        value = (inner_match[1] ?? inner_match[2]) //""や''に対応するため??を使用
                                        .replaceAll("&lt;", '<')
                                        .replaceAll("&gt;", '>')
                                        .replaceAll("&apos;", "'")
                                        .replaceAll("&quot;", '"')
                                        .replaceAll("&amp;", '&')
                                        .replace(/\\/g, '');//[や]のエスケープに

                        tmp_list.push(value);
                    }
                    value = tmp_list;
                }
                catch (e) {
                }
            }
            else {
                value = value.replaceAll("&lt;", '<')
                            .replaceAll("&gt;", '>')
                            .replaceAll("&apos;", "'")
                            .replaceAll("&quot;", '"')
                            .replaceAll("&amp;", '&')
                            .replace(/\\/g, '');
            }
            // console.log("attribute: "+key+": "+value);

            if (key==="p" && !isNaN(value) && value !== ''){
                value = parseFloat(value);
            }

            attributes[key] = value;
        }

        return attributes;
    }

    /**
     * ネスト構造を構築
     */
    buildNestStructure() {
        console.log("=========== buildNestStructure() ============");
        const stack = [];
        const structuredCommands = [];

        for (const command of this.metaCommands) {
            if (command.type === 'open') {
                // 子要素を格納する配列を初期化
                command.children = [];
                command.parent = stack.length > 0 ? stack[stack.length - 1] : null;
                
                if (command.parent) {
                    command.parent.children.push(command);
                } else {
                    structuredCommands.push(command);
                }
                
                stack.push(command);
            } else if (command.type === 'close') {
                // スタックから対応する開始タグを探す
                let found = false;
                for (let i = stack.length - 1; i >= 0; i--) {
                    if (stack[i].command === command.command) {
                        stack[i].closeTag = command;
                        stack.splice(i, 1);
                        found = true;
                        break;
                    }
                }
                if (!found) {
                    this.errors.push(`No matching open tag for close tag: ${command.raw}`);
                }
            } else if (command.type === 'self-closing') {
                // 自己終了タグは直前のノード（textNode または self-closing）を
                // 自分の child に取り込み、自分がその位置に置き換わる
                // 例: textNode, <sc1/>, <sc2/>
                //   → sc1.children=[textNode], sc2.children=[sc1]
                command.children = [];
                command.parent = stack.length > 0 ? stack[stack.length - 1] : null;

                const siblings = command.parent
                    ? command.parent.children
                    : structuredCommands;

                // 直前の兄弟ノードを child として取り込む
                if (siblings.length > 0) {
                    const prev = siblings[siblings.length - 1];
                    siblings.pop();

                    if (prev.command === 'textNode') {
                        // textNodeは「最後の行だけ」をchildrenに取り込み、
                        // それより前の行は兄弟として残す
                        // 例: "line1\nline2\nline3 " → 残す:"line1\nline2\n" 取込:"line3 "
                        const lastNewline = prev.raw.lastIndexOf('\n');
                        if (lastNewline !== -1) {
                            const remainNode = {
                                ...prev,
                                raw: prev.raw.slice(0, lastNewline + 1)
                            };
                            remainNode.parent = command.parent;
                            siblings.push(remainNode);

                            prev.raw = prev.raw.slice(lastNewline + 1);
                        }
                    }
                    // self-closingの場合はそのままchildrenへ（分割不要）

                    prev.parent = command;
                    command.children.push(prev);

                }

                if (command.parent) {
                    command.parent.children.push(command);
                } else {
                    structuredCommands.push(command);
                }
            } else if (command.type === 'textNode') {
                // 自己完結型
                command.parent = stack.length > 0 ? stack[stack.length - 1] : null;
                
                if (command.parent) {
                    command.parent.children.push(command);
                } else {
                    structuredCommands.push(command);
                }
            }

        }

        // 未閉じのタグをチェック
        if (stack.length > 0) {
            for (const unclosed of stack) {
                this.errors.push(`Unclosed tag: ${unclosed.command}:${unclosed.raw}`);
            }
        }

        this.metaCommands = structuredCommands;
    }

    /**
     * パース結果を見やすい形式で表示
     */
    printStructure(commands = this.metaCommands, indent = 0) {
        const result = [];
        const spaces = '  '.repeat(indent);

        for (const cmd of commands) {
            let line = `${spaces}${cmd.command}`;
            
            if (Object.keys(cmd.attributes || {}).length > 0) {
                line += `: ${JSON.stringify(cmd.attributes)}`;
            }
            
            if (cmd.command==="textNode"){
                line += ` (${cmd.raw})`;
            }
            else {
                line += ` (${cmd.type})`;
            }

            result.push(line);

            if (cmd.children && cmd.children.length > 0) {
                result.push(...this.printStructure(cmd.children, indent + 2));
            }
        }

        return result;
    }

    /**
     * 
     */
    reset_random_values(command = this.metaCommands) {
        for (const cmd of command){

            if (cmd.exec_rand) {
                delete cmd.exec_rand;
            }
            if (cmd.select_rand) {
                delete cmd.select_rand;
            }

            if (cmd.children && cmd.children.length > 0) {
                this.reset_random_values(cmd.children);
            }
        }
    }
        /**
     * 
     */
    printQuiz(random_seed) {

        this.reset_random_values();
        this.result = [];
        this.ctx = [];

        Math.seedrandom(random_seed);
        this.render();

        return this.result.join("");        
    }  

    /**
     * 
     */
    render(commands = this.metaCommands){
        for (const cmd of commands) {
            if (cmd.command === 'textNode'){

                let html = cmd.raw;
                //metaタグは，ツリーの先頭から順番に反映させていくversion
                // for (const ctx of this.ctx){
                //     html = this.modify(html, ctx);                    
                // }

                //ツリーの一番奥から順番に反映させるversion
                for (const ctx of [...this.ctx].reverse()){
                    html = this.modify(html, ctx);                    
                }
                if (html && html!=="")
                    this.result.push(html);
            }
            else {
                if (cmd.command === 'select'){

                    if (cmd.children && cmd.children.length > 0){
                        const optionItems = cmd.children.filter(item => item.command === "option");

                        if (optionItems.length>0){
                            cmd.rand = Math.random();
                            const child = optionItems[Math.floor(cmd.rand * optionItems.length)];

                            if (child.children && child.children.length > 0){
                                this.render(child.children);
                            }
                        }
                    }
                }
                else if (cmd.command === 'option'){
                    // console.log("option!!");
                }
                else if (cmd.command === 'flip') {
                    this._calc_prob(cmd);
                    
                    if (!(cmd.children && cmd.children.length > 0))
                        return;
                    const ele_array = cmd.children.filter(item => item.command === "flipElement");
                    if (!(ele_array.length>0))
                        return;

                    if (cmd.exec_rand<cmd.attributes.p){
                        for (let i=ele_array.length-1; i>=0; i--){
                            const child = ele_array[i];
                            if (!(child.children && child.children.length > 0))
                                continue;

                            this.render(child.children);
                        }
                    }
                    else{
                        for (let i=0; i<ele_array.length; i++){
                            const child = ele_array[i];
                            if (!(child.children && child.children.length > 0))
                                continue;

                            this.render(child.children);
                        }
                    }
                }
                else if (cmd.command === 'flipElement'){
                    // console.log("flipElement!!");
                }
                else if (cmd.command === 'includeBlock'){
                    this._calc_prob(cmd);

                    if (cmd.exec_rand<cmd.attributes.p){
                        if (cmd.children && cmd.children.length > 0){
                                this.render(cmd.children);
                        }
                    }
                }
                else {
                    this.ctx.push(cmd);

                    if (cmd.children && cmd.children.length > 0)
                        this.render(cmd.children);

                    this.ctx.pop();
                }
            }
        }
    }

    /**
     * 
     */
    _calc_prob(ctx){
        if (!('p' in ctx.attributes)){
            ctx.attributes.p = 1.0;
        }

        if (!('exec_rand' in ctx)){
            // console.log("recalc_prob");
            ctx.exec_rand = Math.random();
        }

        if (!('select_rand' in ctx)){
            ctx.select_rand = Math.random();
        }
    }
    
    /**
     * 
     */
    modify(html, ctx){

        if (!html)
            return "";

        function _changeToInput(html, target, answer, wordMode){

            if (wordMode){
                return _replaceWord(html, target, `{@${answer}@}`);
            }
            else {
                if (!target.includes("\\"))
                    target = _escapeRegex(target);

                return html.replace(
                    new RegExp(`${target}`, 'g'), 
                    `{@${answer}@}`
                );
            }
        }

        function _replaceWord(html, key, replacement) {
            // 単語境界を使って完全一致のみ置換
            return html.replace(new RegExp(`\\b${_escapeRegex(key)}\\b`, 'g'), replacement);
        }

        function _escapeRegex(string) {
           if (typeof string === 'string')
                return string.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
           else
                return string;
        }

        if (ctx.command==="replace"){
            this._calc_prob(ctx);

            if (ctx.exec_rand>=ctx.attributes.p)
                return html;

            let replacement = ctx.attributes.with[Math.floor(ctx.select_rand*ctx.attributes.with.length)];
            let target = ctx.attributes.target;

            if (typeof target === "string"){
               return html.replaceAll(target, replacement);
            }
            else if (Array.isArray(target)){
                for (const e of target){
                    if (typeof e === "string"){
                        html = html.replaceAll(e, replacement);
                    }
                }
            }
            return html;
        }
        else if (ctx.command==="replaceWord"){
            this._calc_prob(ctx);
            if (ctx.exec_rand>=ctx.attributes.p)
                return html;

            let replacement = ctx.attributes.with[Math.floor(ctx.select_rand*ctx.attributes.with.length)];
            let target = ctx.attributes.target;

            if (typeof target === "string")
               return _replaceWord(html, target, replacement);
            else if (Array.isArray(target)){
                for (const e of target){
                    if (typeof e === "string"){
                        html = _replaceWord(html, e, replacement);
                    }
                }
            }
            return html;
        }
        else if (ctx.command==="skipLine"){
            this._calc_prob(ctx);
            if (ctx.exec_rand<=ctx.attributes.p){
            //     if (ctx.children && ctx.children.length > 0){
            //             this.render(ctx.children);                        
            //     }
                return html;
            }
            else {             

                //行をスキップし，直前の改行もなしにする
                let e = this.result.pop();
                // console.log(e.replaceAll("\n","\\n"));
                e = e.endsWith('\n') ? e.slice(0, -1) : e;
                // console.log(e.replaceAll("\n","\\n"));
                this.result.push(e)

                return "";
            }
        }
        else if (ctx.command==="blankWord"){
            this._calc_prob(ctx);
            if (ctx.exec_rand>=ctx.attributes.p)
                return html;

            let target = ctx.attributes.candidates[Math.floor(ctx.select_rand*ctx.attributes.candidates.length)];

            if (typeof target === "string")
               return _changeToInput(html, target, target, true);
            // else if (Array.isArray(target)){
            //     for (const e in target){//##
            //         console.log(e);
            //         if (typeof e === "string")
            //             html = _changeToInput(html, e, target, true);
            //     }
            // }
            return html;
        }
        else if (ctx.command==="blank"){
            this._calc_prob(ctx);
            if (ctx.exec_rand>=ctx.attributes.p)
                return html;

            let target = ctx.attributes.candidates[Math.floor(ctx.select_rand*ctx.attributes.candidates.length)];

            if (typeof target === "string")
               return _changeToInput(html, target, target, false);
            // else if (Array.isArray(target)){
            //     for (const e in target){//##
            //         if (typeof e === "string")
            //             html = _changeToInput(html, e, target, false);
            //     }
            // }
            return html;
        }
        else if (ctx.command==="replaceAndBlankWord"){
            // _calc_prob();
            this._calc_prob(ctx);
            if (ctx.exec_rand>=ctx.attributes.p)
                return html;

            let replacement = ctx.attributes.with[Math.floor(ctx.select_rand*ctx.attributes.with.length)];
            let target = ctx.attributes.target;

            if (typeof target === "string")
               return _changeToInput(html, target, replacement, true);
            // else if (Array.isArray(target)){
            //     for (const e in target){
            //         if (typeof e === "string")
            //             html = _changeToInput(html, e, replacement, true);
            //     }
            // }
            return html;
        }
        else if (ctx.command==="replaceAndBlank"){
            this._calc_prob(ctx);
            if (ctx.exec_rand>=ctx.attributes.p)
                return html;

            let replacement = ctx.attributes.with[Math.floor(ctx.select_rand*ctx.attributes.with.length)];
            let target = ctx.attributes.target;

            if (typeof target === "string")
               return _changeToInput(html, target, replacement, false);
            // else if (Array.isArray(target)){
            //     for (const e in target){
            //         if (typeof e === "string")
            //             html = _changeToInput(html, e, replacement, false);
            //     }
            // }
            return html;
        }
    }

    /**
     * 特定のコマンドタイプで検索
     */
    findCommandsByType(commandType, commands = this.metaCommands) {
        const results = [];
        
        for (const cmd of commands) {
            if (cmd.command === commandType) {
                results.push(cmd);
            }
            
            if (cmd.children) {
                results.push(...this.findCommandsByType(commandType, cmd.children));
            }
        }
        
        return results;
    }

    /**
     * エラー情報を取得
     */
    getErrors() {
        return this.errors;
    }
}

// # <meta[replace] target=["_FUNC1_"] with=["foo","bar","baz"]>
// # <meta[select]>
// # <meta[option]>
// def _FUNC1_(s=1):# <meta[replace] p="1.0" target="s=1" with=["s","s=1","s=2","s=3","s=4"] /><meta[replace] p="0.2" target=":" with=[""] />
//     print(f"s={s}")

// _FUNC1_(2)# <meta[replace] p="1.0" target="2" with=["", "1", "2"] />
// # </meta[option]>
// # <meta[option]>
// def _FUNC1_(name='d'):# <meta[replace] p="1.0" target="name='d'" with=["name='d'","name"] />
//     print(f"{name}")
//     return name # <meta[skipline] p="0.5" />

// _FUNC1_(a)# <meta[replace] p="1.0" target="a" with=["", "'a'", "'b'"] />
// # </meta[option]>
// # </meta[select]>
// # </meta[replace]>
