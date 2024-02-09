#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ftw.h>

// A global variable to store the file name to search for
char *filename; //store the name of the file that you want to search for

// A callback function for nftw()
int search_file(const char *path, const struct stat *sb, int flag, struct FTW *ftwbuf)
{
    // Check if the current file matches the file name
    if (strcmp(path + ftwbuf->base, filename) == 0)
    {
        // Print the absolute path of the file
        printf("%s\n", path);
        // Return a non-zero value to stop the traversal
        return 1;
    }
    // Return zero to continue the traversal
    return 0;
}

int main(int argc, char *argv[])
{
    // Check the number of arguments
    if (argc != 3)
    {
        fprintf(stderr, "Usage: %s [root_dir] filename\n", argv[0]);
        exit(EXIT_FAILURE);
    }

    // Store the root directory and the file name
    char *root_dir = argv[1];
    filename = argv[2];

    // Call nftw() to traverse the directory tree
    int result = nftw(root_dir, search_file, 10, 0);

    // Check the result of nftw()
    if (result == 0)
    {
        // No file was found
        printf("Search Unsuccessful\n");
    }
    else if (result == -1)
    {
        // An error occurred
        perror("nftw");
        exit(EXIT_FAILURE);
    }

    // Exit successfully
    return 0;
}
