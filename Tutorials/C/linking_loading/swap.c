extern int buf[]; /* This is not a defination but a declaration */

void swap()
{
  int temp;
  temp = buf[1]; /* reference to buf */
  buf[1] = buf[0];
  buf[0] = temp;
}
