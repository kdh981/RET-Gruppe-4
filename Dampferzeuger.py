from tespy.networks import Network
from tespy.components import (Source, Sink, CombustionChamber, Turbine, Compressor, Drum, HeatExchanger, Pump)
from tespy.connections import Connection, Bus, Ref
from CoolProp.CoolProp import PropsSI as CPSI
from tespy.tools import ExergyAnalysis

# fluids
water = {'H2O': 1}
fld_air = {'O2': 0.21, 'N2': 0.79}
fld_gas = {'CH4': 1}

# network
steamgenerator = Network(T_unit='C', p_unit='bar', h_unit='kJ / kg', m_unit='kg / s')

# components of system Turbine
cmp_cp = Compressor('Compressor')
cmp_cc = CombustionChamber('combustion chamber')
cmp_tb = Turbine('Turbine')
src_air = Source('air source')
src_gas = Source('fuel source')
snk_fg = Sink('flue gas sink')

# components of system Steamgenerator
cmp_eco1 = HeatExchanger('economiser')
cmp_pmp1 = Pump('pumpe')
cmp_eva1 = HeatExchanger('evaporator')
cmp_dr1 = Drum('Trommel1')
src_H2O = Source('water')
snk_H20 = Sink('steam')

# connection Turbine System
c01 = Connection(src_air, 'out1', cmp_cp, 'in1', label='01')
c02 = Connection(cmp_cp, 'out1', cmp_cc, 'in1', label='02')
c03 = Connection(src_gas, 'out1', cmp_cc, 'in2', label='03')
c04 = Connection(cmp_cc, 'out1', cmp_tb, 'in1', label='04')
c05 = Connection(cmp_tb, 'out1', cmp_eva1, 'in1', label='05')
c06 = Connection(cmp_eva1, 'out1', cmp_eco1, 'in1', label='06')
c07 = Connection(cmp_eco1, 'out1', snk_fg, 'in1', label='07')

steamgenerator.add_conns(c01, c02, c03, c04, c05, c06, c07)

#connection Evaporator
D1 = Connection(src_H2O, 'out1', cmp_pmp1, 'in1', label='D1')
D2 = Connection(cmp_pmp1, 'out1', cmp_eco1, 'in2', label='D2')
D3 = Connection(cmp_eco1, 'out2', cmp_dr1, 'in1', label='D3')
D4 = Connection(cmp_dr1, 'out1', cmp_eva1, 'in2', label='D4')
D5 = Connection(cmp_eva1, 'out2', cmp_dr1, 'in2', label='D5')
D6 = Connection(cmp_dr1, 'out2', snk_H20, 'in1', label='D6')

steamgenerator.add_conns(D1, D2, D3, D4, D5, D6)


# components Data Turbine System
cmp_cp.set_attr(eta_s=0.8)
cmp_tb.set_attr(eta_s=0.9)
cmp_cc.set_attr(lamb=2)

#components Data Evaporator
cmp_pmp1.set_attr(eta_s=0.8)
cmp_eco1.set_attr(pr1=1, pr2=1)
cmp_eva1.set_attr(pr1=1)

#data Turbine connections
c01.set_attr(p=1, T=15, fluid=fld_air)
c03.set_attr(T=15, m=3, p=30, fluid=fld_gas)
#c04.set_attr(T=1600)
c07.set_attr(p=1)

#data Evaporator1 connections
D1.set_attr(T=60, p=1, m=25, fluid=water)
D2.set_attr(p=40)
D3.set_attr(h=CPSI('H', 'Q', 0, 'P', 40*1e5, 'water')/1e3)
D5.set_attr(h=CPSI('H', 'Q', 1, 'P', 40*1e5, 'water')/1e3)
#D5.set_attr(x=0.6)

# results
steamgenerator.solve(mode='design')
steamgenerator.print_results()

c03.set_attr(m=None)
cmp_eco1.set_attr(ttd_l=20)

steamgenerator.solve(mode='design')
steamgenerator.print_results()

