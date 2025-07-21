/**
 * CIS1703 Programming 2
 * Coursework 2 - Calculator
 * 
 * Filip Kordas - 25734636
 * Gareth Madoc-Jones - 25646648
 * Kasty Regi - 25710729
 * Kate Regi - 25709054
 * 
 * Class "CalcGUI" instantiates a Graphics Interface window, including button input functionality
 */

import javax.swing.*; // Imports java interface for input methods
import javax.swing.text.Position;

import java.awt.*; // Imports "Java Abstract Window Toolkit" - API to develop GUIs
import java.awt.event.*; // Contains all classes for creating user interfaces & painting graphics/images
import java.io.FileWriter;
import java.io.PrintWriter;
import java.io.FileInputStream;
import java.io.FileReader;
import java.util.InputMismatchException;
import java.util.Scanner;
import java.util.Font;

// Implementing ActionListener allows for inputs //
public class CalcGUI implements ActionListener {
    // Class Variables //
    JFrame frame; // Creates frame variable for GUI
    JTextField text; // Creates text field for output
    JButton[] numButtons = new JButton[10]; // Creates array for number buttons [0-9]
    JButton[] functionButtons = new JButton[10]; // Creates array for function buttons [+, -, *, /, ., =, Clear]
    JButton[] storageButtons = new JButton[8]; // Creates array for storage buttons [A, B, C, D]
    JButton add, subtract, multiply, divide, // Number buttons
            decimal, clear, undo, equal, // Function buttons
            storA, storB, storC, storD, Inverse, Sign_Switch,
            root, squared; // Storage buttons
    JPanel panel; // Creates panel to place & order buttons

    double Astor = 0, Bstor = 0, Cstor = 0, Dstor = 0; // Storage variables
    double num1 = 0, num2 = 0, result = 0, func; // Calculation variables
    char operator; // Text value for function buttons

    public CalcGUI() {
        // Creates a window titled "Calculator", width 600px by 770px //
        frame = new JFrame("Calculator");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(600, 770);
        frame.setLayout(null);

        // Creates a Text Field - This is where output will be presented //
        text = new JTextField();
        text.setBounds(50, 25, 500, 60);
        text.setEditable(false);
        text.setFont(new Font("arial", java.awt.Font.PLAIN, 24));

        // Assigns Buttons with their variables & assigned text //
        storageButtons[0] = storA = new JButton("A");
        storageButtons[1] = storB = new JButton("B");
        storageButtons[2] = storC = new JButton("C");
        storageButtons[3] = storD = new JButton("D");
        storageButtons[4] = Inverse = new JButton("1/x");
        storageButtons[5] = Sign_Switch = new JButton("+/-");
        storageButtons[6] = squared = new JButton("xʸ");
        storageButtons[7] = root = new JButton("√x");
        functionButtons[0] = add = new JButton("+");
        functionButtons[1] = subtract = new JButton("-");
        functionButtons[2] = multiply = new JButton("x");
        functionButtons[3] = divide = new JButton("÷");
        functionButtons[4] = decimal = new JButton(".");
        functionButtons[5] = equal = new JButton("=");
        functionButtons[6] = clear = new JButton("CLEAR");
        functionButtons[7] = undo = new JButton("UNDO");

        // For each number button, Will count input once clicked //
        for (int i = 0; i < 10; i++) {
            numButtons[i] = new JButton(String.valueOf(i)); // Assigns buttons with text
            numButtons[i].addActionListener(this);
            numButtons[i].setFocusable(false);
            numButtons[i].setFont(new Font("arial", java.awt.Font.PLAIN, 20));
        }

        // For each function button, Will count input once clicked //
        for (int i = 0; i < 8; i++) {
            functionButtons[i].addActionListener(this);
            functionButtons[i].setFocusable(false);
            functionButtons[i].setFont(new Font("arial", java.awt.Font.PLAIN, 20));
        }

        // For each storage button, Will count input once clicked //
        for (int i = 0; i < 8; i++) {
            storageButtons[i].addActionListener(this);
            storageButtons[i].setFocusable(false);
            storageButtons[i].setFont(new Font("arial", java.awt.Font.PLAIN, 20));
        }

        clear.setBounds(400, 110, 150, 50); // Creates button for "Clear" command
        undo.setBounds(50,110,150,50);  // Creates button for "Undo" Command

        // Creates GUI Grid which stores all number & function buttons //
        panel = new JPanel();
        panel.setBounds(50, 175, 500, 500);
        panel.setLayout(new GridLayout(6, 4, 10, 10));

        /* COLUMN 1 */ /* COLUMN 2 */ /* COLUMN 3 */ /* COLUMN 4 */
        /* ROW 1 */ panel.add(storA);
        panel.add(storB);
        panel.add(storC);
        panel.add(storD);
        panel.add(root);
        panel.add(squared);
        panel.add(Inverse);
        panel.add(Sign_Switch);

        /* ROW 2 */ panel.add(numButtons[7]);
        panel.add(numButtons[8]);
        panel.add(numButtons[9]);
        panel.add(add);
        /* ROW 3 */ panel.add(numButtons[4]);
        panel.add(numButtons[5]);
        panel.add(numButtons[6]);
        panel.add(subtract);
        /* ROW 4 */ panel.add(numButtons[1]);
        panel.add(numButtons[2]);
        panel.add(numButtons[3]);
        panel.add(multiply);
        /* ROW 5 */ panel.add(numButtons[0]);
        panel.add(decimal);
        panel.add(equal);
        panel.add(divide);

        // Adds TextField & Buttons to Calculator Window //
        frame.add(text);
        frame.add(clear);
        frame.add(undo);
        frame.add(panel);
        frame.setVisible(true);
    }

    // Main Startup Code //
    public static void main(String[] args) throws Exception {
        new CalcGUI();
    }

    // When a button is pressed, this object is called: //
    public void actionPerformed(ActionEvent input) {
        for (int i = 0; i < 10; i++) {
            if (input.getSource() == numButtons[i]) {
                text.setText(text.getText() + i);

                /**
                 * Compiled by Gareth Madoc-Jones Adapted from Calculator Program in Java
                 * Swing/JFrame with Source Code [Online] Available from:
                 * https://www.tutorialsfield.com/simple-calculator-program-in-java-using-swing/?utm_content=cmp-true
                 * I did not copy the code instead using it as background research into
                 * performing the task.
                 */
            }
        }

        if (input.getSource() == decimal) {
            text.setText(text.getText() + ".");
        }

        if (input.getSource() == add) {
            try {
                num1 = Double.parseDouble(text.getText());
                func = 1;
                text.setText("");
            } catch (Exception e) {
                JOptionPane.showMessageDialog(frame,
                        "Please only click operation button once. Click a number to continue.","ERROR", JOptionPane.ERROR_MESSAGE); 
                System.out.println("ERROR. Please only click operation button once. Click a number to continue.");
            } /**
               * Compiled by Gareth Madoc-Jones This was adapted from Java GUI Calculator
               * Tutorial (New) Part4: Operations [Online] Available from:
               * https://www.youtube.com/watch?v=Wy_RMWi8w20 [Accessed 8th March 2024]
               * Error Message code adapted from Java Message Box Available from:
               * https://www.roseindia.net/java/example/java/swing/MessageBox.shtml?expand_article=1 and https://stackoverflow.com/questions/26300862/how-to-show-an-error-message-in-java-in-a-friendly-way 
               * [Accessed 8th March]
               */
        }
        if (input.getSource() == subtract) {
            try {
                num1 = Double.parseDouble(text.getText());
                func = 2;
                text.setText("");
            } catch (Exception e) {
                JOptionPane.showMessageDialog(frame,
                        "Please only click operation button once. Click a number to continue.","ERROR", JOptionPane.ERROR_MESSAGE);
                System.out.println("ERROR. Please only click operation button once. Click a number to continue.");
            }
            /**
             * // Compiled by Gareth Madoc-Jones This was adapted from Java GUI Calculator
             * Tutorial (New) Part4: Operations [Online] Available from:
             * https://www.youtube.com/watch?v=Wy_RMWi8w20 [Accessed 8th March 2024] and Rose India (2024) Error Message Box Available from:  
             * https://www.roseindia.net/java/example/java/swing/MessageBox.shtml?expand_article=1
             * [Accessed 8th March]
             */
        }
        if (input.getSource() == multiply) {
            try {
                num1 = Double.parseDouble(text.getText());
                func = 3;
                text.setText("");
            } catch (Exception e) {
                
                JOptionPane.showMessageDialog(frame,
                        "Please only click operation button once. Click a number to continue.","ERROR", JOptionPane.ERROR_MESSAGE); 
                System.out.println("ERROR. Please only click operation button once. Click a number to continue.");
            }
            // Compiled by Kasty Regi
        }
        if (input.getSource() == divide) {
            try {
                num1 = Double.parseDouble(text.getText());
                func = 4;
                text.setText("");
            } catch (Exception e) {
                JOptionPane.showMessageDialog(frame,
                        "Please only click operation button once. Click a number to continue.","ERROR", JOptionPane.ERROR_MESSAGE); 
                System.out.println("ERROR. Please only click operation button once. Click a number to continue.");
            }
            // Compiled by Kate Regi
        }
        if (input.getSource() == squared) {
            try {
                num1 = Double.parseDouble(text.getText());
                func = 5;
                text.setText("");
            } catch (Exception e) {
                JOptionPane.showMessageDialog(frame,
                        "There is no input variable. Click a number to continue.","ERROR", JOptionPane.ERROR_MESSAGE); 
                System.out.println("ERROR. There is no input variable. Click a number to continue.");
            }
            // Compiled by Filip Kordas
        }
        if (input.getSource() == equal) {
            try {num2 = Double.parseDouble(text.getText()); // The func double is used to set the operation for the
                                                            // calculator to perform.
                if (func == 1) {
                    result = num1 + num2; // Compiled by Gareth Madoc-Jones This was adapted from Java GUI Calculator
                                        // Tutorial (New) Part4: Operations [Online] Available from:
                                        // https://www.youtube.com/watch?v=Wy_RMWi8w20 [Accessed 8th March 2024]
                    text.setText(String.valueOf(result));
                    num1 = result;

                    if (num2 < 0) {
                        result = num1 - (-num2);
                        text.setText(String.valueOf(result));
                        num1 = result;
                    }
                } else if (func == 2) {
                    result = num1 - num2;
                    text.setText(String.valueOf(result));
                    num1 = result;
                    if (num2 < 0) {
                        func =1;
                        result = num1 + (-num2);
                        text.setText(String.valueOf(result));
                        num1 = result;
                    }
                } else if (func == 3) {
                    result = num1 * num2;
                    num1 = result;
                    text.setText(String.valueOf(result));
                    num1 = result;
                } else if (func == 4) {
                    result = num1 / num2;
                    text.setText(String.valueOf(result));
                    num1 = result;
                    if (num2 ==0) {
                        JOptionPane.showMessageDialog(frame,
                        "You cannot divide by 0","ERROR", JOptionPane.ERROR_MESSAGE); // failsafe to prevent dividing by 0
                        System.out.println("ERROR. You cannot divide by 0.");
                        text.setText("");
                    }
                } else if (func == 5) {
                    result = Math.pow(num1,num2);
                    num1 = result;
                    text.setText(String.valueOf(result));
                }
            }
            catch (Exception e) {
                JOptionPane.showMessageDialog(frame,
                            "To Complete another calculation click an operation","ERROR", JOptionPane.ERROR_MESSAGE);
                    System.out.println("ERROR. To Complete another calculation click an operation.");
            }
        }
        if (input.getSource() == clear) {
            text.setText(""); // If "Clear" button pressed; All values within the JTextField are removed The storage functions are wiped as well.
            Astor = 0;
            Bstor = 0;
            Cstor = 0;
            Dstor = 0;
        }
        if (input.getSource() == undo) {
            try {                                                                                           // Compiled By Gareth Madoc-Jones
                text.setText(text.getText().substring(0,text.getText().length()-1));  // Adapted from Stack Overflow (2014) Java Calculator how to make backspace [Online] Available from https://stackoverflow.com/questions/26516378/java-calculator-how-to-make-backspace [Accessed 11th March 2024]
            } catch (Exception e) {
                JOptionPane.showMessageDialog(frame,
                "There is nothing to undo","ERROR", JOptionPane.ERROR_MESSAGE);
                System.out.println("ERROR. There is nothing to undo.");
            }
        }
        if (input.getSource() == storA) {
            // Compiled by Filip Kordas
            if (text.getText().equals("")) {
            text.setText(String.valueOf(Astor));
            } else {
                Astor = Double.parseDouble(text.getText());
                text.setText("");
            }
        }

        if (input.getSource() == storB) {
            // Compiled by Filip Kordas
            if (text.getText().equals("")) {
            text.setText(String.valueOf(Bstor));
            } else {
                Bstor = Double.parseDouble(text.getText());
                text.setText("");
            }
        }

        if (input.getSource() == storC) {
                // Compiled by Filip Kordas
            if (text.getText().equals("")) {
                text.setText(String.valueOf(Cstor));
            } else {
                Cstor = Double.parseDouble(text.getText());
                text.setText("");
            }
        }

        if (input.getSource() == storD) {
           // Compiled by Filip Kordas
            if (text.getText().equals("")) {
                text.setText(String.valueOf(Dstor));
            } else {
                Dstor = Double.parseDouble(text.getText());
                text.setText("");
            }
    
        }
        if (input.getSource() == Inverse) {
            try {num2 = Double.parseDouble(text.getText());
                double inverse = 1 / num2;
                String inverse_number = Double.toString(inverse);
                text.setText(inverse_number);
            }
            catch (Exception e) {
                JOptionPane.showMessageDialog(frame,"There is nothing to invert", "ERROR", JOptionPane.ERROR_MESSAGE); // failsafe to prevent negative number root error.
                System.out.println("ERROR. There is nothing to invert");
            }
        }
        if (input.getSource() == Sign_Switch) {
            try {text.setText("" + (-1 * Double.parseDouble(text.getText()))); // adapted from Patrick Feltes (2014)  Java GUI Calculator Tutorial (NEW) Part4: Operations[Online] Available from: https://www.youtube.com/watch?v=Wy_RMWi8w20 [Accessed 12th March]
            }
            catch (Exception e) {JOptionPane.showMessageDialog(frame,
                "There is nothing to switch","ERROR", JOptionPane.ERROR_MESSAGE);
                System.out.println("ERROR. There is nothing to Switch.");
            }
        }
        if (input.getSource() == root) {                       // Compiled By Gareth Madoc-Jones
            try { num2 = Double.parseDouble(text.getText());    // Adapted from Tutorials Field (2022). Calculator Program in Java Swing / JFrame | Calculator Application Using Java with Source Code [Online] Available from https://www.youtube.com/watch?v=ZhEaf_aEG04[Accessed 11th March ]
                double root = Math.sqrt(num2);
                String root_number = Double.toString(root);
                text.setText(root_number);
                if (num1 < 0 || num2 <0) {
                    JOptionPane.showMessageDialog(frame,"Cannot root a negative", "ERROR", JOptionPane.ERROR_MESSAGE); // failsafe to prevent negative number root error.
                    System.out.println("ERROR. You cannot root a negative");
                    text.setText("");
                }
            } catch (Exception e ) {
            JOptionPane.showMessageDialog(frame,
            "There is nothing to root","ERROR", JOptionPane.ERROR_MESSAGE);
            System.out.println("ERROR. There is nothing to root.");
            }
        }
    }
}


// REFERENCES //
/**
 * GUI Structure code by Filip Kordas
 * Adapted from: Youtube - "Bro Code", [Online] Available at:
 * https://youtu.be/dfhmTyRTCSQ?si=74NllRM10hfpvTAj (Accessed 06/03/2024)
 * 
 * Numbered Buttons by Gareth Madoc-Jones
 * Research from: Swing/JFrame with Source Code [Online] Available at:
 * https://www.tutorialsfield.com/simple-calculator-program-in-java-using-swing/?utm_content=cmp-true (Accessed 08/03/2024)
 * 
 * Addition + Subtraction by Gareth Madoc-Jones
 * Patrick Feltes (2014) Tutorial (NEW) Part4: Operations [Online] Available at:
 * https://www.youtube.com/watch?v=Wy_RMWi8w20 (Accessed 08/03/2024)
 * 
 * Error Message Handling by Gareth Madoc-Jones
 * Rose India (2024) Java Message Box, Available at:
 * https://www.roseindia.net/java/example/java/swing/MessageBox.shtml?expand_article=1 and https://stackoverflow.com/questions/26300862/how-to-show-an-error-message-in-java-in-a-friendly-way  (Accessed 08/03/2024)
 * 
 * Undo by Gareth Madoc-Jones
 * Adapted from: Stack Overflow (2014) Java Calculator how to make a backspace, [Online] Available at: 
 * https://stackoverflow.com/questions/26516378/java-calculator-how-to-make-backspace (Accessed 11/03/2024)
 * 
 * Square Root by Gareth Madoc-Jones
 * Adapted from Tutorial Field (2022) Calculator Program in Java Swing / JFrame | Calculator Application Using Java with Source Code, [Online] Available at:
 * https://www.youtube.com/watch?v=ZhEaf_aEG04 (Accessed 11/03/2024)
 */
