from tespy.networks import Network
from tespy.components import (Source, Sink, CombustionChamber, Turbine, Compressor, Drum, HeatExchanger, Pump, SimpleHeatExchanger, Valve, Pipe, Splitter, Merge, CycleCloser)
from tespy.connections import Connection, Bus, Ref
from CoolProp.CoolProp import PropsSI as CPSI
from tespy.tools import ExergyAnalysis

# fluids
water = {'H2O': 1}
fld_air = {'O2': 0.21, 'N2': 0.79}
fld_gas = {'CH4': 1}
vapor = {'H2O': 1}

# network
steamgenerator = Network(T_unit='C', p_unit='bar', h_unit='kJ / kg', m_unit='kg / s')

# components of system Turbine
cmp_cp = Compressor('Compressor')
cmp_cc = CombustionChamber('combustion chamber')
cmp_tb = Turbine('Turbine')
src_air = Source('air source')
src_gas = Source('fuel source')
snk_fg = Sink('flue gas sink')

# components of system Steamgenerator nr.1
cmp_eco1 = HeatExchanger('economiser1')
cmp_pmp1 = Pump('pumpe1')
cmp_eva1 = HeatExchanger('evaporator1')
cmp_dr1 = Drum('Trommel1')
src_H2O = Source('water1')
snk_H20 = Sink('steam1')

# components of system Steamgenerator nr.2
cmp_eco2 = HeatExchanger('economiser2')
cmp_pmp2 = Pump('pumpe2')
cmp_eva2 = HeatExchanger('evaporator2')
cmp_dr2 = Drum('Trommel2')
src2_H2O = Source('water2')
snk2_H20 = Sink('steam2')

#Speisewasserbehälter + Entgaser
cmp_entgaser = Merge('Entgaser')
cmp_pumpe = Pump('pumpe0')
cmp_pipe = Pipe('Dampf zugabe')
cmp_split2 = Splitter('Massentrennung1')
cmp_split3 = Splitter('Massentrennung2')
src_Dampf = Source('Vapor')
src_Kondensat = Source('Kondensat')
cmp_drossel = Valve('Drossel')

# connection Turbine System
c01 = Connection(src_air, 'out1', cmp_cp, 'in1', label='01')
c02 = Connection(cmp_cp, 'out1', cmp_cc, 'in1', label='02')
c03 = Connection(src_gas, 'out1', cmp_cc, 'in2', label='03')
c04 = Connection(cmp_cc, 'out1', cmp_tb, 'in1', label='04')
c05 = Connection(cmp_tb, 'out1', cmp_eva1, 'in1', label='05')
c06 = Connection(cmp_eva1, 'out1', cmp_eco1, 'in1', label='06')
c07 = Connection(cmp_eco1, 'out1', cmp_eva2, 'in1', label='07')
c08 = Connection(cmp_eva2, 'out1', cmp_eco2, 'in1', label='08')
c09 = Connection(cmp_eco2, 'out1', snk_fg, 'in1', label='09')

steamgenerator.add_conns(c01, c02, c03, c04, c05, c06, c07, c08, c09)

#Speisewasserbehälter
S1 = Connection(src_Kondensat, 'out1', cmp_pumpe, 'in1', label='S1')
S2 = Connection(cmp_pumpe, 'out1', cmp_entgaser, 'in1', label='S2')
S3 = Connection(cmp_drossel, 'out1', cmp_entgaser, 'in2', label='S3')
S4 = Connection(cmp_entgaser, 'out1', cmp_split2, 'in1', label='S4')

steamgenerator.add_conns(S1, S2, S3, S4)

#connection Evaporator nr.1
D11 = Connection(cmp_split2, 'out1', cmp_pmp1, 'in1', label='D11')
D12 = Connection(cmp_pmp1, 'out1', cmp_eco1, 'in2', label='D12')
D13 = Connection(cmp_eco1, 'out2', cmp_dr1, 'in1', label='D13')
D14 = Connection(cmp_dr1, 'out1', cmp_eva1, 'in2', label='D14')
D15 = Connection(cmp_eva1, 'out2', cmp_dr1, 'in2', label='D15')
D16 = Connection(cmp_dr1, 'out2', snk_H20, 'in1', label='D16')

steamgenerator.add_conns(D11, D12, D13, D14, D15, D16)

#connection Evaporator nr.2
D21 = Connection(cmp_split2, 'out2', cmp_pmp2, 'in1', label='D21')
D22 = Connection(cmp_pmp2, 'out1', cmp_eco2, 'in2', label='D22')
D23 = Connection(cmp_eco2, 'out2', cmp_dr2, 'in1', label='D23')
D24 = Connection(cmp_dr2, 'out1', cmp_eva2, 'in2', label='D24')
D25 = Connection(cmp_eva2, 'out2', cmp_dr2, 'in2', label='D25')
D26 = Connection(cmp_dr2, 'out2', cmp_split3, 'in1', label='D26')
D27 = Connection(cmp_split3, 'out1', cmp_drossel, 'in1', label='D27')
D28 = Connection(cmp_split3, 'out2', snk2_H20, 'in1', label='D28')

steamgenerator.add_conns(D21, D22, D23, D24, D25, D26, D27, D28)


# components Data Turbine System
cmp_cp.set_attr(eta_s=0.8)
cmp_tb.set_attr(eta_s=0.9)
cmp_cc.set_attr(lamb=2)

#data Turbine connections
c01.set_attr(p=1, T=15, fluid=fld_air)
c03.set_attr(T=15, m=40, p=30, fluid=fld_gas)
c09.set_attr(p=1)

#Data Speisewasserbehälter
cmp_pumpe.set_attr(eta_s=0.8)

#Data Speisewasserbehälter Connections
S1.set_attr(T=60, p=1, m=350, fluid=water)
S2.set_attr(p=4)
S3.set_attr(h=CPSI('H', 'Q', 1, 'P', 4*1e5, 'water')/1e3)
#S3.set_attr(p=4)


#components Data Evaporator nr.1
cmp_pmp1.set_attr(eta_s=0.8)
cmp_eco1.set_attr(pr1=1, pr2=1)
cmp_eva1.set_attr(pr1=1)

#data Evaporator nr.1 connections
D11.set_attr(m=100)
D12.set_attr(p=15)
D13.set_attr(h=CPSI('H', 'Q', 0, 'P', 15*1e5, 'water')/1e3)
D15.set_attr(h=CPSI('H', 'Q', 1, 'P', 15*1e5, 'water')/1e3)


#components Data Evaporator nr.2
cmp_pmp2.set_attr(eta_s=0.8)
cmp_eco2.set_attr(pr1=1, pr2=1)
cmp_eva2.set_attr(pr1=1)

#data Evaporator nr.2 connections
D22.set_attr(p=5)
D23.set_attr(h=CPSI('H', 'Q', 0, 'P', 5*1e5, 'water')/1e3)
D25.set_attr(h=CPSI('H', 'Q', 1, 'P', 5*1e5, 'water')/1e3)
D28.set_attr(m=250)

# results
steamgenerator.solve(mode='design')
steamgenerator.print_results()

print('Nächste Rechnung')

#was machst dieser Schritt genau ?
c03.set_attr(m=None)
cmp_eco2.set_attr(ttd_l=25)
cmp_cc.set_attr(lamb=None)
c04.set_attr(T=1600)

steamgenerator.solve(mode='design')
steamgenerator.print_results()

