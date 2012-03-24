public class double2stringrepresentation { 
        public static void main(String args[]) {
                double d =2.0;
                String s = (long) d == d ? "" + (long) d : "" + d; 

                System.out.println(s);

        }

}

