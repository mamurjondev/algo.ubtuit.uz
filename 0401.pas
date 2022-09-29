var x,a,b:longint;
c,s,w:real;
begin
read(x,a,b);
c:=16*x+a;
s:=x*x*ln(a*x)/ln(2);
w:=exp(a*x)+cos(b*x);
if (x>4)then writeln(c:2:2)else if(x>=2)and(x<=4)then writeln(s:2:2)else 
if(x<2)then write (w:2:2);
end.    
