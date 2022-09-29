    var
    a, x, y: real;
begin
    read(x, y);
    a := abs(x + 1) * (x + 2 * y) / (abs(x + 1) * y * y + abs(y * y + 2)) + 2 * x - y;
    write(a:0:2);
end.    
