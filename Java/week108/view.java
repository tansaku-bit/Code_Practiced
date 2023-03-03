//第8週用サンプルプログラム
import java.awt.Button;
import java.awt.Choice;
import java.awt.FlowLayout;
import java.awt.Frame;
import java.awt.TextField;

public class View2 {
    private Frame f5;
    private Button add2;
    private TextField name2;
    private Choice index2;
    private Choice priority2;

    public View2() {
        f5 = new Frame();
        index2 = new Choice();     //今回ポップアップメニューに変更してみた
        name2 = new TextField(15);
        priority2 = new Choice();  //今回ポップアップメニューに変更してみた
        add2 = new Button("add");
        //添字用ポップアップメニューの項目を作る
        for (int i = 0; i < 10; i++) {
            index2.add(String.valueOf(i));
        }
        //優先度用ポップアップメニューの項目を作る
        for (int i = 1; i <= 5; i++) {
            priority2.add(String.valueOf(i));
        }
        //フレームに部品を追加して表示
        f5.setLayout(new FlowLayout());
        f5.add(index2);
        f5.add(name2);
        f5.add(priority2);
        f5.add(add2);
        f5.pack();
        f5.setVisible(true);
    }
    public static void main(String[] args) {
        new View2();

    }