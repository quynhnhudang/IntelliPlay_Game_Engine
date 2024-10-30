#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Function declarations
void initializeGame();
void gameLoop();
void renderGraphics();
void processInput();
void updateNPCBehavior();

int isRunning = 1; // Global variable to control game loop

int main() {
    initializeGame();
    gameLoop();
    printf("Game Ended.\n");
    return 0;
}

// Initializes game settings and configurations
void initializeGame() {
    srand(time(NULL));
    printf("Game Initialized.\n");
}

// Main game loop that manages rendering, input, and AI updates
void gameLoop() {
    while (isRunning) {
        renderGraphics();
        processInput();
        updateNPCBehavior();
        printf("Running Game Loop...\n");
    }
}

// Placeholder for graphics rendering logic
void renderGraphics() {
    printf("Rendering Graphics...\n");
    // Additional rendering logic for game objects goes here
}

// Handles user input and checks for exit commands
void processInput() {
    char command;
    printf("Enter command (q to quit): ");
    command = getchar();
    getchar();  // Clear the newline character
    if (command == 'q') {
        isRunning = 0;  // Exit game loop
    }
}

// Calls AI module for NPC behavior updates
void updateNPCBehavior() {
    printf("Updating NPC Behavior...\n");
    // In an actual setup, here we'd call the Python script for AI
    system("python3 ai_module.py");  // Example command to call AI module
}
