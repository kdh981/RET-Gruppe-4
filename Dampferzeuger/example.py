from tespy.networks import Network
from tespy.components import (Sink, Source, CombustionChamber, HeatExchanger, Drum, Pump, Compressor, Turbine)
from tespy.connections import Connection
from CoolProp.CoolProp import PropsSI as CP

# fluids
air = {'O2': 0.21, 'N2': 0.79}
fuel = {'CH4': 1}
water = {'H2O': 1}

# network
gtsteamboiler = Network(T_unit='C', p_unit='bar', h_unit='kJ / kg', m_unit='kg / s')

# components
src_air = Source('air-source')
src_fuel = Source('fuel-source')
snk_fluegas = Sink('flue-gas-sink')
src_water = Source('water')
snk_steam = Sink('steam')
src_water2 = Source('water2')
snk_steam2 = Sink('steam2')
cmp_comp = Compressor('air-compressor')
cmp_cc = CombustionChamber('combustion chamber')
cmp_exp = Turbine('expander')
cmp_pump = Pump('pump')
cmp_econ = HeatExchanger('economizer')
cmp_drum = Drum('drum')
cmp_evap = HeatExchanger('evaporator')
cmp_pump2 = Pump('pump2')
cmp_econ2 = HeatExchanger('economizer2')
cmp_drum2 = Drum('drum2')
cmp_evap2 = HeatExchanger('evaporator2')

# connections
c11 = Connection(src_air, 'out1', cmp_comp, 'in1', label='11 (air)')
c12 = Connection(cmp_comp, 'out1', cmp_cc, 'in1', label='12 (compressed air)')
c13 = Connection(src_fuel, 'out1', cmp_cc, 'in2', label='13 (fuel)')
c14 = Connection(cmp_cc, 'out1', cmp_exp, 'in1', label='14 (hot and compressed fluegas)')
c15 = Connection(cmp_exp, 'out1', cmp_evap, 'in1', label='15 (fluegas)')
c16 = Connection(cmp_evap, 'out1', cmp_econ, 'in1', label='16 (fluegas)')
c17 = Connection(cmp_econ, 'out1', cmp_evap2, 'in1', label='17 (fluegas)')
c18 = Connection(cmp_evap2, 'out1', cmp_econ2, 'in1', label='18 (fluegas)')
c19 = Connection(cmp_econ2, 'out1', snk_fluegas, 'in1', label='19 (fluegas)')

c21 = Connection(src_water, 'out1', cmp_pump, 'in1', label='21 (water, lq.)')
c22 = Connection(cmp_pump, 'out1', cmp_econ, 'in2', label='22 (water, lq.)')
c23 = Connection(cmp_econ, 'out2', cmp_drum, 'in1', label='23 (water, x=0)')
c24 = Connection(cmp_drum, 'out1', cmp_evap, 'in2', label='24 (drum circulation)')
c25 = Connection(cmp_evap, 'out2', cmp_drum, 'in2', label='25 (drum circulation)')
c26 = Connection(cmp_drum, 'out2', snk_steam, 'in1', label='26 (steam, x=1)')

c31 = Connection(src_water2, 'out1', cmp_pump2, 'in1', label='31 (water, lq.)')
c32 = Connection(cmp_pump2, 'out1', cmp_econ2, 'in2', label='32 (water, lq.)')
c33 = Connection(cmp_econ2, 'out2', cmp_drum2, 'in1', label='33 (water, x=0)')
c34 = Connection(cmp_drum2, 'out1', cmp_evap2, 'in2', label='34 (drum circulation)')
c35 = Connection(cmp_evap2, 'out2', cmp_drum2, 'in2', label='35 (drum circulation)')
c36 = Connection(cmp_drum2, 'out2', snk_steam2, 'in1', label='36 (steam, x=1)')

gtsteamboiler.add_conns(c11,c12,c13,c14,c15,c16,c17,c18,c19,c21,c22,c23,c24,c25,c26,c31,c32,c33,c34,c35,c36)

# parameters

# components
cmp_comp.set_attr(eta_s=0.8, pr=20)
cmp_cc.set_attr(lamb=2.5)
cmp_exp.set_attr(eta_s=0.9)
cmp_pump.set_attr(eta_s=0.8)
cmp_econ.set_attr(pr1=1, pr2=1)
cmp_evap.set_attr(pr1=1)
cmp_pump2.set_attr(eta_s=0.8)
cmp_econ2.set_attr(pr1=1, pr2=1)
cmp_evap2.set_attr(pr1=1)

# connections
c11.set_attr(p=1, T=25, fluid=air)
c13.set_attr(m=18, T=25, fluid=fuel)
c19.set_attr(p=1)
c21.set_attr(m=25, p=1, T=60, fluid=water)
c22.set_attr(p=40)
c23.set_attr(h=CP('H', 'P', 40*1E5, 'Q', 0, 'water')/1E3)
c25.set_attr(x=0.6)
c31.set_attr(m=100, p=1, T=60, fluid=water)
c32.set_attr(p=14)
c33.set_attr(h=CP('H', 'P', 14*1E5, 'Q', 0, 'water')/1E3)
c35.set_attr(x=0.6)


# solve
gtsteamboiler.solve(mode='design')
gtsteamboiler.print_results()

c13.set_attr(m=None)
cmp_econ2.set_attr(ttd_l=20)

gtsteamboiler.solve(mode='design')
gtsteamboiler.print_results()


