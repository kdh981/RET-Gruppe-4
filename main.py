from tespy.networks import Network
from tespy.components import (Source, Sink, DiabaticCombustionChamber, Turbine, Compressor, Drum, HeatExchanger, Pump)
from tespy.connections import Connection, Bus, Ref
from CoolProp.CoolProp import PropsSI as CPSI
from tespy.tools import ExergyAnalysis

# fluids
H20 = 'water'
fld_H20 = {H20: 1}

air = 'air'
fld_air = {'O2': 0.21, 'N2': 0.79}
fld_gas = {'CH4': 1}

# network
steamgenerator = Network(T_unit='C', p_unit='bar', h_unit='kJ / kg', m_unit='kg / s')

# components of system Turbine
cmp_cp = Compressor('Compressor')
cmp_cc = DiabaticCombustionChamber('combustion chamber')
cmp_tb = Turbine('Turbine')
src_air = Source('air source')
src_gas = Source('fuel source')
snk_fg = Sink('flue gas sink')

# components of system Steamgenerator
cmp_eco1 = HeatExchanger('economiser')
cmp_pmp1 = Pump('pumpe')
cmp_eva1 = HeatExchanger('evaporator')
cmp_dr1 = Drum('Trommel1')
src_H2O = Source('water source')
snk_H20 = Sink('water sink')

# components Data Turbine System
cmp_cp.set_attr(eta_s=0.8, pr=1)
cmp_tb.set_attr(eta_s=0.9)
cmp_cc.set_attr(lamb=1.05)

#components Data Evaporator
cmp_pmp1.set_attr(eta_s=0.8)
cmp_eco1.set_attr(pr1=1, pr2=1)
cmp_eva1.set_attr(pr1=1, pr2=1)

# connection Turbine System
c01 = Connection(src_air, 'out1', cmp_cp, 'in1', label='01')
c02 = Connection(cmp_cp, 'out1', cmp_cc, 'in1', label='02')
c03 = Connection(src_gas, 'out1', cmp_cc, 'in2', label='03')
c04 = Connection(cmp_cc, 'out1', cmp_tb, 'in1', label='04')
c05 = Connection(cmp_tb, 'out1', cmp_eva1, 'in2', label='05')
c06 = Connection(cmp_eva1, 'out2', cmp_eco1, 'in2', label='06')
c07 = Connection(cmp_eco1, 'out2', snk_fg, 'in1',label='07')

steamgenerator.add_conns(c01, c02, c03, c04, c05, c06, c07)

#data Turbine connections
c01.set_attr(p=1, T=15, fluid=fld_air)
c03.set_attr(T=15, p=30, m=1, fluid=fld_gas)
c05.set_attr(p=1)

#connection Evaporator
D1 = Connection(src_H2O, 'out1', cmp_pmp1, 'in1', label='D1')
D2 = Connection(cmp_pmp1, 'out1', cmp_eco1, 'in1', label='D2')
D3 = Connection(cmp_eco1, 'out1', cmp_dr1, 'in1', label='D3')
D4 = Connection(cmp_dr1, 'out1', cmp_eva1, 'in1', label='D4')
D5 = Connection(cmp_eva1, 'out1', cmp_dr1, 'in2', label='D5')
D6 = Connection(cmp_dr1, 'out2', snk_H20, 'in1', label='D6')

steamgenerator.add_conns(D1, D2, D3, D4, D5, D6)

#data Evaporator1
D1.set_attr(T=15, p=1, m=25, fluid=fld_H20)
D2.set_attr(p=40)
D3.set_attr(T=150)
h4 = CPSI('H', 'Q', 0, 'P', 40*1e5, H20) / 1e3
D4.set_attr(h=h4)
h_sat = CPSI('H', 'Q', 1, 'P', 40*1e5, H20) / 1e3
D6.set_attr(h=h_sat)



# results
steamgenerator.solve(mode='design')
steamgenerator.print_results()
