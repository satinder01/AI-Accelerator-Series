module mac (
    input clk,
    input reset,
    input [7:0] a_in,      // Activation from SRAM
    input [7:0] b_in,      // Weight from SRAM
    output reg [15:0] out  // Accumulator (Partial Sum)
);
    always @(posedge clk) begin
        if (reset)
            out <= 16'b0;
        else
            out <= out + (a_in * b_in);
    end

// Add this for waveform generation
    initial begin
        $dumpfile("dump.vcd");
        $dumpvars(0, mac);
    end
endmodule
