/*
 * Copyright 2013 Netherlands eScience Center
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */


import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;

/**
 * @author Jason Maassen <J.Maassen@esciencecenter.nl>
 * @version 1.0
 * @since 1.0
 *
 */
public class Server {

    private static final short DEFAULT_PORT = 19876;
    
    private ServerSocket ss;
    private BufferedReader input;
    
    public Server(File inputfile, short port) throws IOException {
        input = new BufferedReader(new FileReader(inputfile));
        ss = new ServerSocket(port, 1024);
    }

    public void run() throws IOException { 

        boolean done = false;
        
        System.out.println("Server starting!");
        
        while (!done) {
            String line = input.readLine();
            
            if (line == null) {
                // We've reached EOF!
                input.close();
                done = true;
            } else if (!line.startsWith("#")) {
                Socket tmp = ss.accept();
                System.out.println("Returning line: " + line);
                tmp.getOutputStream().write((line+"\n").getBytes()); 
                tmp.close();
            }
        }

        System.out.println("No more input -- shutting down");
        ss.close();
    }

    public static void main(String [] args) {

        short port = DEFAULT_PORT;

        if (args.length < 1 || args.length > 2) { 
            System.err.println("Usage nls.esciencecenter.patty.Server <inputfile> [port]");
            System.exit(1);
        }

        File f = new File(args[0]);

        if (!f.exists() || !f.isFile() || !f.canRead()) { 
            System.err.println("Cannot access inputfile " + args[0]);
            System.exit(1);
        }

        if (args.length == 2) { 
            port = Short.parseShort(args[1]);
        }

        try { 
            Server s = new Server(f, port);
            s.run();
        } catch (Exception e) { 
            System.err.println("Server failed: " + e.getLocalizedMessage());
            e.printStackTrace(System.err);
            System.exit(1);
        }

    }
}

