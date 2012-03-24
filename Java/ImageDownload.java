import java.io.File;
import java.awt.image.BufferedImage;
import javax.imageio.ImageIO;
import java.net.URL;
class ImageDownload{


        public static void main(String[] args) throws java.io.IOException{
                String path = "C:\\image.jpg";
                URL url = new URL("http://www.analoghype.com/wp-content/uploads/2011/07/spotify.jpg");
                BufferedImage image = ImageIO.read(url);
                ImageIO.write(image, "jpg", new File(path));


        }



}









