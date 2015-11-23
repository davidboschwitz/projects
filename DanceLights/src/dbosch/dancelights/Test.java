/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package dbosch.dancelights;

/**
 *
 * @author davidboschwitz
 */
public class Test {

    public static void main(String... args) {
        for (int a = 0; a < 10; a++) {
            for (int b = 0; b < 10; b++) {
                String a_ = Integer.toBinaryString(a);
                while(a_.length() < 4)
                    a_ = '0' + a_;
                String b_ = Integer.toBinaryString(b);
                while(b_.length() < 4)
                    b_ = '0' + b_;
                String r = Integer.toBinaryString(a ^ b);
                while(r.length() < 4)
                    r = '0' + r;
                
                System.out.println(a_ + "^" + b_ + "=" + r);
            }
        }
    }
}
