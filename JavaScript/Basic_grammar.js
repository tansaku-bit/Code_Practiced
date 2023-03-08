//変数及び定数の定義
let variable = 12;
const constant = 24;
var oldtype_variable = 36;

/*
letで変数、constで定数を定義できる。
varはES6以前に使われていた宣言方法であり、現在はletとconstがモダンな宣言方法。
varは再宣言も再代入も可能であり、JavaScriptにおいて影響範囲が広い宣言方法である。そのため、意図しない再宣言や再代入によるエラーに繋がる可能性がある。
また、letとconstがブロック（{}で囲んだ範囲）ごとに作られるスコープ内で利用できるのに対し、varは関数内でのみ利用できる関数スコープや全てのスコープで利用できるグローバルスコープに該当する。
varはletとconstとは違う動作をするため、基本的に使わない方がエラーを防止できる。
*/



//配列の定義
let Aptenodytes = ['emperor', 'king'];
const Pygoscelis = ['adelie', 'chinstrap', 'gentoo'];

/*
変数や定数を定義するのと同じように、[]で複数の値を配列として格納できる。
配列の要素はコンマ（,）で区切り、最初の要素を0番目として表す。
*/



//実行結果の表示
console.log(Aptenodytes[0]); // => emperor

/*
JavaScriptで実行結果を確認したい場合、ConsoleAPIを使うことが多い。
console.log(引数)で引数の結果をコンソールに表示する。
*/



//ループ文・繰り返し
for(let f_roop = 0; f_roop>5 ; f_roop++){
    console.log(f_roop);
}
let w_roop = 0;
while(w_roop > 5){
    console.log(w_roop);
    w_roop++;
}

/*
繰り返しにはwhile文とfor文の2種類の方法がある。
for文は
for(初期化式; 条件式; 増分式){
    実行する命令;
}
while文は
while(条件式){
    実行する命令;
}
繰り返し文は中にある命令を実行するたびに条件式の判定を行う。
条件式がtrue（真）の場合は再度実行し、条件式がfalse（偽）の場合は終了する。
trueとは終了する条件を満たしていない、falseは終了する条件を見たした状態を言う。
条件式が常にtrueの場合、無限ループが発生しサーバーなどに負荷を掛けてしまうため注意が必要。
*/



//if/else文
if(Pygoscelis != null){
    console.log(Pygoscelis);
} else {
    console.log(Aptenodytes);
}

/*
if文は条件式を満たしたときと満たさないときで実行したい命令を分けられる。
if(条件式)の条件式を満たしたとき、その命令が実行される。
elseはif文が偽のときに実行される。elseは単体での使用が出来ない。
*/



//関数の宣言
const demo1_func = () => {
    console.log(Aptenodytes[0], 'penguin');
};
function demo2_func(){
    console.log(Aptenodytes[0], 'penguin');
}
let demo3_func = new Function(console.log(Aptenodytes[0], 'penguin'));
/*
関数は同じ命令を何度も使いたいときや、任意のタイミングで実行させたいときに利用される。
いずれの関数も処理結果自体は同じだが、定義の方法が違う。
demo1はアロー演算子を用いた定義方法で、アロー演算子の前の()に引数を入れる。
demo2はfunctionのキーワードを使った関数の定義方法で、関数名の後ろにある()に引数を入れる。
demo3はFunctionコンストラクタを使用した関数の定義方法で、()内に引数と命令をまとめて入れる。Functionコンストラクタを使用した場合、カンマで要素を区切り最後の要素が命令になる。処理を複数入れたい場合は、同一の要素内にセミコロンで区切った複数の命令を記述する
*/



//オブジェクト
const Otani_san = {
    country: 'Japan',
    team: 'Samurai Japan',
    number: '16'
};
console.log(Otani_san.number); //オブジェクトOtani_sanのnumberをコンソールに表示
/*
オブジェクトは複数のデータを1つの塊として持つことができる。
オブジェクトではキー（プロパティ名）と値を1つのペアとして管理し、キーと値の1つのペアをプロパティと呼ぶ。オブジェクトとはプロパティの塊とも言い換えられる。
*/



//windowオブジェクトとdocumentオブジェクト
console.log(window.innerHeight);
window.alert('詐欺サイトで良く見るやつ!');
document.getElementsByTagName('button')[0].addEventListener('click', ()=> {
    window.alert('安易にボタンを押さないでね');
});
/*
デフォルトで設定されているオブジェクト。
windowはWebブラウザ全体のオブジェクト。表示しているブラウザのデータを引っ張ってくることが出来る。
documentは表示しているページ全体のオブジェクトで、HTMLのタグなどを指定し参照したいときに使うgetElementsByTagNameなどがある。
今回の命令では、HTMLのbuttonタグの1番目がクリックされた時、window.alertが出るようになっている。
*/