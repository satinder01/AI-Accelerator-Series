import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge

@cocotb.test()
async def mac_test(dut):
    # Create a 10ns clock on the 'clk' port
    clock = Clock(dut.clk, 10, units="ns")
    cocotb.start_soon(clock.start())

    # Reset hardware
    dut.reset.value = 1
    await RisingEdge(dut.clk)
    dut.reset.value = 0

    # Test Data: (1*10) + (2*20) + (3*30) = 140
    activations = [1, 2, 3]
    weights = [10, 20, 30]

    for a, w in zip(activations, weights):
        dut.a_in.value = a
        dut.b_in.value = w
        await RisingEdge(dut.clk)

    await RisingEdge(dut.clk)
    
# Now check the result
    actual_value = dut.out.value.integer # Convert from Binary to Integer
    print(f"Hardware Result: {actual_value}")
    assert actual_value == 140
