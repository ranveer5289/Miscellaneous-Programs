import javax.swing.JFrame;
import javax.swing.JOptionPane;

public class BasicDialogBox { 
    public static void main ( String [] args ) { 

        JFrame frame = new JFrame("My dialog asks....");

        frame.setUndecorated( true );
        frame.setVisible( true );
        frame.setLocationRelativeTo( null );


        String message = JOptionPane.showInputDialog(frame,
            "Would this be enough?.", 
            "My dialog asks....", 
            JOptionPane.INFORMATION_MESSAGE);

        System.out.println( "Got " + message );

        frame.dispose();
    }
}


