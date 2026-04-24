import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles, Timer


@cocotb.test()
async def test_project(dut):
    dut._log.info("Start D Latch Test")

    clock = Clock(dut.clk, 10, units="us")
    cocotb.start_soon(clock.start())

    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 1

    # d = 0, e = 1 => q follows d = 0
    dut.ui_in[0].value = 0
    dut.ui_in[1].value = 1
    await Timer(20, units="ns")
    assert dut.uo_out[0].value == 0

    # d = 1, e = 1 => q follows d = 1
    dut.ui_in[0].value = 1
    dut.ui_in[1].value = 1
    await Timer(20, units="ns")
    assert dut.uo_out[0].value == 1

    # e = 0, q should hold 1 even if d changes to 0
    dut.ui_in[1].value = 0
    dut.ui_in[0].value = 0
    await Timer(20, units="ns")
    assert dut.uo_out[0].value == 1

    # e = 1 again, q should follow d = 0
    dut.ui_in[1].value = 1
    await Timer(20, units="ns")
    assert dut.uo_out[0].value == 0

    # e = 0, q should hold 0 even if d changes to 1
    dut.ui_in[1].value = 0
    dut.ui_in[0].value = 1
    await Timer(20, units="ns")
    assert dut.uo_out[0].value == 0

    await ClockCycles(dut.clk, 5)
    dut._log.info("D Latch Test Completed")
