class Solution {
    public String interpret(String command) {
        String s = "";
        for (int i = 0; i < command.length() - 1; i++){
            System.out.println(i);
            if (command.charAt(i) == 'G')
                s += "G";
            else if (command.charAt(i) == '(' && command.charAt(i + 1) == 'a')
                s += "al";
            else if (command.charAt(i) == '(' && command.charAt(i + 1) == ')')
                s += "o";
        }
        if (command.charAt(command.length() - 1) == 'G')
            s += "G";
        return s;
    }
}