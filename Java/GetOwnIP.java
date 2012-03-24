import java.util.*;
import java.lang.*;
import java.net.*;

public class GetOwnIP
{
        public static void main(String args[]) throws java.net.UnknownHostException{ 
                try{
                        InetAddress ownIP=InetAddress.getLocalHost();
                        System.out.println("IP of my system is := "+ownIP.getHostAddress());
                        System.out.println("IP of my system is := "+ownIP.toString());
                }catch (Exception e){
                        System.out.println("Exception caught ="+e.getMessage());
                }
                System.out.println(InetAddress.getByName("10.100.56.27").getCanonicalHostName().toString());
        }
}

