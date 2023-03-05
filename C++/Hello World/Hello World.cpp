#include <chrono>
#include <iostream>

int main() {
    int max_counter = 1000000000;
    std::cout << "Hello World, let's count to " << max_counter << std::endl;
    int counter = 0;
    auto start_time = std::chrono::high_resolution_clock::now();
    while (counter <= max_counter) {
        counter += 1;
        if (counter == max_counter) {
            std::cout << std::endl << "Finished" << std::endl << std::endl;
        }
    }
    auto stop_time = std::chrono::high_resolution_clock::now();
    auto duration = std::chrono::duration_cast <std::chrono::seconds>(stop_time - start_time);
    std::cout << "Loop ran for: " << duration.count() << " seconds." << std::endl;
    return 0;
}
