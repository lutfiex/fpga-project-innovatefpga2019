//declare the Verilog module - The inputs and output signals.
module mux5to1(    
	 Data_in_0,
    Data_in_1,
	 Data_in_2,
    Data_in_3,
	 Data_in_4,
    set,
    Data_out
    );

    //what are the input ports.
    input  [11:0] Data_in_0;
    input  [11:0] Data_in_1;
	 input  [11:0] Data_in_2;
	 input  [11:0] Data_in_3;
	 input  [11:0] Data_in_4;
    input  [2:0] set;
    //What are the output ports.
    reg [11:0] Data_out;
    //Internal variables.

    

    //Always block - the statements inside this block are executed when the given sensitivity list 
    //is satidfied. for example in this case the block is executed when any changes occur in the three signals 
    //named 'Data_in_0','Data_in_1' or 'sel'.
initial
  begin
    case (set)
		 
      default : Data_out <= Data_in_0;
		3'b000  : Data_out <= Data_in_0;
      3'b001  : Data_out <= Data_in_1;
      3'b010  : Data_out <=  Data_in_2;
      3'b011  : Data_out <=  Data_in_3;
		3'b100  : Data_out <=  Data_in_4;	
    endcase
  end
    
endmodule