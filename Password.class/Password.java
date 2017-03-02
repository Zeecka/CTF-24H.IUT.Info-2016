/*
 * Decompiled with CFR 0_118.
 */
import java.io.InputStream;
import java.io.PrintStream;
import java.util.Scanner;

class Password {
    static int N = 19;
    static int[] crypted_pass = new int[]{16, 15, 16, 29, 29, 22, 30, 1, 5, 26, 16, 1, 6, 25, 19, 86, 86, 93, 92};
    static String key = "vcqztxhdwiukgordbsm";

    Password() {
    }

    public static void main(String[] arrstring) {
        System.out.print("Veuillez saisir le mot de passe : ");
        Scanner scanner = new Scanner(System.in);
        String string = scanner.nextLine();
        boolean bl = false;
        while (!bl) {
            try {
                Thread.sleep(1000);
                bl = true;
            }
            catch (InterruptedException var4_4) {}
        }
        boolean bl2 = true;
        if (string.length() != N) {
            bl2 = false;
        }
        for (int i = 0; i < N && bl2; ++i) {
            if ((string.charAt(i) ^ key.charAt(i)) == crypted_pass[i]) continue;
            bl2 = false;
        }
        if (bl2) {
            System.out.println("Gagn\u00e9, vous avez trouv\u00e9 le flag !");
        } else {
            System.out.println("Perdu, d\u00e9sol\u00e9.");
        }
    }
}