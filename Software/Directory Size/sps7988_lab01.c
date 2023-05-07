
#include <stdio.h>
#include <string.h>
#include <dirent.h>
#include <sys/stat.h>

// calculate Size of file storesult at location path
int directorySize(char path[])
{
    FILE *fp = fopen(path, "r");
    fseek(fp, 0L, SEEK_END);
    int result;
    result = ftell(fp);
    fclose(fp);
    return result;
}
// merge directory
void dir(char tot[], char dir1[], char dir2[])
{
    strcpy(tot, dir1);
    strcat(tot, "/");
    strcat(tot, dir2);
}
float opdir(char dir_name[])
{
    float totalSize = 0;
    char tot[1024];
    // defining directory structure
    struct dirent *de;
    // checking whether the path contains file or directory
    struct stat typeofdir;
    DIR *dr = opendir(dir_name);
    if (dr == NULL)
    {
        printf("Directory not found");
        return 0;
    }
    // Navigate the directory if it exists
    while ((de = readdir(dr)) != NULL)
    {
        // skip parent directory
        if (strcmp(de->d_name, ".") == 0)
            continue;
        if (strcmp(de->d_name, "..") == 0)
            continue;
        dir(tot, dir_name, de->d_name);
        stat(tot, &typeofdir);
        // Check for directory
        if (S_ISDIR(typeofdir.st_mode))
        {
            totalSize += opdir(tot);
        }
        else
        {
            // calculate directorySize of file and add to the totalSize
            totalSize += directorySize(tot);
        }
    }
    return totalSize;
}
void main()
{
    float size;
    size = opdir(".");
    printf("\nSize of directory in bytes: %.3f Bytes", size);
}
