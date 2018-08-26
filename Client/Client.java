import java.io.*;
import java.net.*;

public class Client {

	// Middleware socket info
    static String MIDDLEWARE_HOSTNAME = "localhost";
    static int    MIDDLEWARE_PORT     = 9999;

    public static void main(String[] args) throws IOException {
    	// Create message from params
    	String message = String.join(" ", args);

        String result = request(message);
        System.out.println(result);
    }

    // Send request to the middleware
    public static String request(String message){
        Socket         socket    = null;
        PrintWriter    socketOut = null;
        BufferedReader socketIn  = null;

        // Create connection
        try {
            socket    = new Socket(MIDDLEWARE_HOSTNAME, MIDDLEWARE_PORT);
            socketOut = new PrintWriter(socket.getOutputStream(), true);
            socketIn  = new BufferedReader(new InputStreamReader(socket.getInputStream()));
        } catch (UnknownHostException e) {
            System.err.println("Unknown host: " + MIDDLEWARE_HOSTNAME);
            System.exit(1);
        } catch (IOException e) {
            System.err.println("Can't connect to the server");
            System.exit(1);
        }

        String result = null;
        try {
            // Send message
            socketOut.println(message);
            result = socketIn.readLine();

            // Close connection
            socketOut.close();
            socketIn.close();
            socket.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
        
        return result;
    }
}