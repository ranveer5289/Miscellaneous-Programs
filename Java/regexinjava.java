import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regexinjava {

        public static void main(String[] args) {
                Pattern p = Pattern.compile("\\$(\\w.*?)\\$");
                String s = "Hello $everybody$. How $are$ you $all$";

                Matcher m = p.matcher(s);
                while (m.find()) {
                        System.out.println(m.group(1));
                }
        }

}

