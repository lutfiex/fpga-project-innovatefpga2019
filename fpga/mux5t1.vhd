library ieee;
    use ieee.std_logic_1164.all;
    use ieee.numeric_std.all;
    use ieee.math_real.all;
entity mux5t1 is
port(
  a     : in  std_logic_vector(0 to 11);
  b     : in  std_logic_vector(0 to 11);
  c     : in  std_logic_vector(0 to 11);
  d     : in  std_logic_vector(0 to 11);
  e     : in  std_logic_vector(0 to 11);
  s     : in  std_logic_vector(0 to 2);
  m     : out std_logic_vector(0 to 11));
end mux5t1;
architecture rtl of mux5t1 is
begin
  p_mux : process(a,b,c,d,e,s)
  begin
    case s is 
      when "001"   => m <= b;
      when "010"   => m <= c;
      when "011"   => m <= d;
		when "100"   => m <= e;
      when others => m <= a;
    end case;
  end process p_mux;
end rtl;