#  High-End Rule-Based Chatbot

##  Concept

A **rule-based chatbot** is a conversational system that works using **predefined rules** and **decision trees**.  
Instead of learning from data (like AI chatbots), it uses conditions such as `if-else` statements to decide how to respond based on the user's input.  

This project demonstrates a **high-end menu-driven customer service chatbot** where users can navigate through multiple service options, similar to an **IVR (Interactive Voice Response)** system used in call centers.

---

##  About the Code

- **Language**: Python  
- **Approach**: Rule-based using `if-else` conditions  
- **Features**:
  - Menu-driven navigation
  - Submenus for specific service areas
  - Return-to-main-menu functionality
  - Randomized polite responses for human-like feel
  - Simulated product info, order support, and technical help

---

##  Working of the Code

1. **Start of the Chat**  
   - The bot welcomes the user with:  
     ` ChatBot: Welcome to High-End Menu-Driven Rule-Based Chatbot!`  
   - Asks for the user's name and stores it for personalized responses.

2. **Main Menu Display**  
   - Shows five options:
     1. Product Information
     2. Order Support
     3. Technical Support
     4. Speak to a Human Agent
     5. Exit

3. **Submenu Navigation**  
   - Each main menu option (except Exit) has its own submenu with further choices.
   - Example:  
     **Order Support** → Track Order, Cancel Order, Return to Main Menu.

4. **User Input Handling**  
   - Bot checks user’s choice and executes the relevant function.
   - Handles invalid inputs with an error message.

5. **Return to Main Menu**  
   - Users can navigate back to the main menu anytime.

6. **Exit**  
   - Bot thanks the user and ends the conversation.

---

##  How We Developed It

1. **Planning**  
   - Selected the chatbot type (**rule-based**).
   - Decided on a **menu-driven** approach for easy navigation.

2. **Menu Structure Design**  
   - Designed a **main menu** and **submenus** for different service areas.

3. **Implementation**  
   - Created functions for each submenu (`product_info()`, `order_support()`, `tech_support()`).
   - Added **randomized polite responses** for natural feel.

4. **Testing**  
   - Verified each menu flow works correctly.
   - Checked error handling for invalid inputs.

---

##  Evaluation

| **Criteria** | **Result** |
|--------------|------------|
| **Functionality** | All menu and submenu options function as intended. |
| **User Experience** | Easy to navigate, clear menus. |
| **Error Handling** | Properly handles invalid input cases. |
| **Personalization** | Greets user by name for friendly tone. |
| **Realism** | Uses randomized responses for a less robotic feel. |

---

##  Future Enhancements

- Add **time-based greetings** (Good Morning/Afternoon/Evening).
- Enable **multi-language support**.
- Store chat history for analytics.
- Integrate real APIs for **live data** (order tracking, product details).

---

##  Example Run

 ChatBot: Welcome to High-End Menu-Driven Rule-Based Chatbot!
May I have your name? Krishna
Hello Krishna! How can I assist you today?

 Main Menu:
1️ Product Information
2️ Order Support
3️ Technical Support
4️ Speak to a Human Agent
5️ Exit
Choose an option: 2

 Order Support Menu:

Track my order

Cancel my order

Return to Main Menu
Enter your choice: 1
Please enter your Order ID: 12345
ChatBot Tracking Order 12345... Estimated delivery: 3 days.
---

##  Flowchart

```mermaid
flowchart TD
    A[Start] --> B[Welcome User & Ask Name]
    B --> C[Show Main Menu]
    C --> D1[1️ Product Information]
    C --> D2[2️ Order Support]
    C --> D3[3️ Technical Support]
    C --> D4[4️ Speak to Human Agent]
    C --> D5[5️ Exit]

    D1 --> E1[Show Product Info Submenu]
    E1 --> C

    D2 --> E2[Show Order Support Submenu]
    E2 --> C

    D3 --> E3[Show Technical Support Submenu]
    E3 --> C

    D4 --> F[Display Randomized Connecting Message]
    F --> C

    D5 --> G[Thank User & End]
