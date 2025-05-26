import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Digite a cadeia w:");
        String w = scanner.nextLine();

        System.out.println("Digite o valor de p:");
        int p = Integer.parseInt(scanner.nextLine());

        if (!pertenceLinguagem(w)) {
            System.out.println("A cadeia não pertence à linguagem.");
            scanner.close();
            return;
        }

        simularDivisoes(w, p);

        scanner.close();
    }

    public static void simularDivisoes(String w, int p) {
        boolean quebraLema = false;

        for (int i = 0; i <= p - 1; i++) { 
            for (int j = 1; j <= p - i && i + j <= w.length(); j++) { 
                String x = w.substring(0, i);
                String y = w.substring(i, i + j);
                String z = w.substring(i + j);

                System.out.println("Divisão: x = '" + x + "', y = '" + y + "', z = '" + z + "'");

                for (int k = 0; k <= 3; k++) { 
                    String wBombeada = x + y.repeat(k) + z;
                    boolean pertence = pertenceLinguagem(wBombeada);
                    System.out.println("  y^" + k + ": '" + wBombeada + "' -> " + (pertence ? "PERTENCE" : "NÃO pertence"));

                    if (!pertence) {
                        quebraLema = true;
                    }
                }
            }
        }

        if (quebraLema) {
            System.out.println("\nHá uma quebra do lema: a linguagem NÃO pode ser regular.");
        } else {
            System.out.println("\nNão foi encontrada quebra do lema para esta cadeia e valor de p.");
        }
    }

    public static boolean pertenceLinguagem(String s) {
        int i = 0;
        while (i < s.length() && s.charAt(i) == 'a') i++;
        int numA = i;
        int numB = 0;
        while (i < s.length() && s.charAt(i) == 'b') {
            i++;
            numB++;
        }
        return i == s.length() && numA == numB;
    }
}