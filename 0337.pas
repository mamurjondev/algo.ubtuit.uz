var n:integer; s,i:real;
begin
read (n);
s:=0;
i:=1;
while i <=n do begin 
s:=s+(3*i*i*i+4*sqr (i)+5*i)/(i*i*i+sqr (i)+i);
i:=i+1;
end;
writeln(s:0:2);
end.    
