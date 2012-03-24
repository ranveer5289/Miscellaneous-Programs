import java.io.*;
import java.net.*;
import java.nio.channels.*;

class downloadfile
{
        public static void main(String[] args) throws IOException
        {


                URL google = new URL("url here");
                ReadableByteChannel rbc = Channels.newChannel(google.openStream());
                FileOutputStream fos = new FileOutputStream("abc.srt");
                fos.getChannel().transferFrom(rbc, 0, 1 << 24);
        }
}

