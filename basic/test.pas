begin
  bh := ToroGetMem(SizeOf(TBufferHead));
  
  If bh = nil then
  begin
    Result := nil;
    Exit;
  end;


end.