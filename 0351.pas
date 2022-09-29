var a,b,c:integer; c1,a1,b1:real;
begin
read(a,b,c);
c1:=1/2*sqrt(2*sqr(a)+2*sqr(b)-sqr(c));
a1:=1/2*sqrt(2*sqr(c)+2*sqr(b)-sqr(a));
b1:=1/2*sqrt(2*sqr(a)+2*sqr(c)-sqr(b));
write(a1:0:2,' ',b1:0:2,' ',c1:0:2);
end.    
