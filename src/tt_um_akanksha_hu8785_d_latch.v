`default_nettype none

module tt_um_akanksha_hu8785_d_latch (
    input  wire [7:0] ui_in,
    output wire [7:0] uo_out,
    input  wire [7:0] uio_in,
    output wire [7:0] uio_out,
    output wire [7:0] uio_oe,
    input  wire       ena,
    input  wire       clk,
    input  wire       rst_n
);
    wire d = ui_in[0];
    wire e = ui_in[1];

    reg q;

    /* verilator lint_off LATCH */
    always @(*) begin
        if (e)
            q = d;
    end
    /* verilator lint_on LATCH */
    assign uo_out[0] = q;
    assign uo_out[1] = 1'b0;
    assign uo_out[2] = 1'b0;
    assign uo_out[3] = 1'b0;
    assign uo_out[4] = 1'b0;
    assign uo_out[5] = 1'b0;
    assign uo_out[6] = 1'b0;
    assign uo_out[7] = 1'b0;

    assign uio_out = 8'b00000000;
    assign uio_oe  = 8'b00000000;

    wire _unused = &{ena, clk, rst_n, ui_in[7:2], uio_in, 1'b0};

endmodule

`default_nettype wire
