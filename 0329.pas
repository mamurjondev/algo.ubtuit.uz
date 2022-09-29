Var n,i,x:Longint;s:real;
 Begin
 Read(n,x);
 s:=0;
 For i:=1 to n do
 s:=s+exp(i*ln(x))/(sqrt(x*i));
 Write(s:2:2);
 End.    
