#include <stdio.h>
int main(int argc, char *argv[]) {
 //char buffer[1] = {0};
 FILE *fp = fopen(argv[1], "rb");
 FILE *gp = fopen(argv[2], "wb");
 if(fp==NULL) printf("No files specified\n");
 if(gp==NULL) printf("No output file specified\n");

 int stream;
 int agete = 0xCC;
 int hibikase;
 while((stream = fgetc(fp))!=EOF) {
 hibikase = stream;
 agete = stream ^ agete;
 fputc(agete, gp);
 }
 fclose(fp);
 fclose(gp);
 return 0;
}
