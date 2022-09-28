const s = 'qwertyuiopasdfghjklzxcvbnmq';
var
    a: char;
begin
    readln(a);
    writeln(s[pos(a, s) + 1]);
end. 
