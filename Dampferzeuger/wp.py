from tespy.networks import Network
from tespy.components import (Source, Sink, CombustionChamber, Turbine, Compressor, Drum, HeatExchanger, Pump, SimpleHeatExchanger, Valve, Pipe, Splitter, Merge, CycleCloser)
from tespy.connections import Connection, Bus, Ref
from CoolProp.CoolProp import PropsSI as CPSI
from tespy.tools import ExergyAnalysis

# fluids
water = {'H2O': 1}
fld_air = {'O2': 0.21, 'N2': 0.79}
fld_gas = {'CH4': 1}
fld_wf = {'R704': 1}


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

# components of system Steamgenerator nr.3
cmp_eco3 = HeatExchanger('economiser3')
cmp_pmp3 = Pump('pumpe3')
cmp_eva3 = HeatExchanger('evaporator3')
cmp_dr3 = Drum('Trommel3')
src3_H2O = Source('water3')
snk3_H20 = Sink('steam3')

#Speisewasserbehälter + Entgaser
cmp_entgaser = Merge('Entgaser')
cmp_pumpe = Pump('pumpe0')
cmp_pipe = Pipe('Dampf zugabe')
cmp_split2 = Splitter('Massentrennung1')
cmp_split3 = Splitter('Massentrennung2')
src_Dampf = Source('Vapor')
src_Kondensat = Source('Kondensat')
cmp_drossel = Valve('Drossel')

#wp
src_wp = Source('src oel')
snk_wp = Sink('snk oel')
cmp_eco_wp1 = HeatExchanger('wpeco1')
cmp_eco_wp2 = HeatExchanger('wpeco2')
cmp_eco_wp3 = HeatExchanger('wpeco3')
cmp_heatsrc = HeatExchanger('Heat Source')
cmp_throttel = Valve('DrosselWP')
cmp_comp = Compressor('WPpumpe')
cyclecloser = CycleCloser('CycleCloser')

# connection Turbine System
c01 = Connection(src_air, 'out1', cmp_cp, 'in1', label='01')
c02 = Connection(cmp_cp, 'out1', cmp_cc, 'in1', label='02')
c03 = Connection(src_gas, 'out1', cmp_cc, 'in2', label='03')
c04 = Connection(cmp_cc, 'out1', cmp_tb, 'in1', label='04')
c05 = Connection(cmp_tb, 'out1', cmp_eva1, 'in1', label='05')
c06 = Connection(cmp_eva1, 'out1', cmp_eco1, 'in1', label='06')
c07 = Connection(cmp_eco1, 'out1', cmp_eva2, 'in1', label='07')
c08 = Connection(cmp_eva2, 'out1', cmp_eco2, 'in1', label='08')
c09 = Connection(cmp_eco2, 'out1', cmp_eva3, 'in1', label='09')
c10 = Connection(cmp_eva3, 'out1', cmp_eco3, 'in1', label='10')
c11 = Connection(cmp_eco3, 'out1', cmp_heatsrc, 'in1', label='11')
c12 = Connection(cmp_heatsrc, 'out1', snk_fg, 'in1', label='12')

steamgenerator.add_conns(c01, c02, c03, c04, c05, c06, c07, c08, c09, c10, c11, c12)

S1 = Connection(src_Dampf, 'out1', cmp_entgaser, 'in1', label='S1')
S2 = Connection(src_Kondensat, 'out1', cmp_pumpe, 'in1', label='S2')
S3 = Connection(cmp_pumpe, 'out1', cmp_entgaser, 'in2', label='S3')
S4 = Connection(cmp_entgaser, 'out1', cmp_split2, 'in1', label='S4')
S5 = Connection(cmp_split2, 'out2', cmp_split3, 'in1', label='S5')

steamgenerator.add_conns(S1, S2, S3, S4, S5)

#connection Evaporator nr.1
D11 = Connection(cmp_split3, 'out1', cmp_pmp1, 'in1', label='D11')
D12 = Connection(cmp_pmp1, 'out1', cmp_eco_wp1, 'in2', label='D12')
D13 = Connection(cmp_eco_wp1, 'out2', cmp_eco1, 'in2', label='D13')
D14 = Connection(cmp_eco1, 'out2', cmp_dr1, 'in1', label='D14')
D15 = Connection(cmp_dr1, 'out1', cmp_eva1, 'in2', label='D15')
D16 = Connection(cmp_eva1, 'out2', cmp_dr1, 'in2', label='D16')
D17 = Connection(cmp_dr1, 'out2', snk_H20, 'in1', label='D17')

steamgenerator.add_conns(D11, D12, D13, D14, D15, D16, D17)

#connection Evaporator nr.2
D21 = Connection(cmp_split3, 'out2', cmp_pmp2, 'in1', label='D21')
D22 = Connection(cmp_pmp2, 'out1', cmp_eco_wp2, 'in2', label='D22')
D23 = Connection(cmp_eco_wp2, 'out2', cmp_eco2, 'in2', label='D23')
D24 = Connection(cmp_eco2, 'out2', cmp_dr2, 'in1', label='D24')
D25 = Connection(cmp_dr2, 'out1', cmp_eva2, 'in2', label='D25')
D26 = Connection(cmp_eva2, 'out2', cmp_dr2, 'in2', label='D26')
D27 = Connection(cmp_dr2, 'out2', snk2_H20, 'in1', label='D27')

steamgenerator.add_conns(D21, D22, D23, D24, D25, D26, D27)

#connection Evaporator nr.3
D31 = Connection(cmp_split2, 'out1', cmp_pmp3, 'in1', label='D31')
D32 = Connection(cmp_pmp3, 'out1', cmp_eco_wp3, 'in2', label='D32')
D33 = Connection(cmp_eco_wp3, 'out2', cmp_eco3, 'in2', label='D33')
D34 = Connection(cmp_eco3, 'out2', cmp_dr3, 'in1', label='D34')
D35 = Connection(cmp_dr3, 'out1', cmp_eva3, 'in2', label='D35')
D36 = Connection(cmp_eva3, 'out2', cmp_dr3, 'in2', label='D36')
D37 = Connection(cmp_dr3, 'out2', snk3_H20, 'in1', label='D37')

steamgenerator.add_conns(D31, D32, D33, D34, D35, D36, D37)

#connection Wärmepumpe
I1 = Connection(cmp_comp, 'out1', cmp_eco_wp1, 'in1', label='I1')
I2 = Connection(cmp_eco_wp1, 'out1', cmp_eco_wp2, 'in1', label='I2')
I3 = Connection(cmp_eco_wp2, 'out1', cmp_eco_wp3, 'in1', label='I3')
I4 = Connection(cmp_eco_wp3, 'out1', cmp_throttel, 'in1', label='I4')
I5 = Connection(cmp_throttel, 'out1', cmp_heatsrc, 'in2', label='I5')
I6 = Connection(cmp_heatsrc, 'out2', cyclecloser, 'in1', label='I6')
I7 = Connection(cyclecloser, 'out1', cmp_comp, 'in1', label='I7')

steamgenerator.add_conns(I1, I2, I3, I4, I5, I6, I7)


# components Data Turbine System
cmp_cp.set_attr(eta_s=0.8)
cmp_tb.set_attr(eta_s=0.9)
cmp_cc.set_attr(lamb=2)
#data Turbine connections
c01.set_attr(p=1, T=15, fluid=fld_air)
c03.set_attr(T=15, m=50, p=30, fluid=fld_gas)
c11.set_attr(p=1)


#components Data Evaporator nr.1
cmp_pmp1.set_attr(eta_s=0.8)
cmp_eco1.set_attr(pr1=1, pr2=1)
cmp_eco_wp1.set_attr(pr1=1, pr2=1)
cmp_eva1.set_attr(pr1=1)
#data Evaporator nr.1 connections
D11.set_attr(m=25)
D12.set_attr(p=41)
D13.set_attr(Td_bp=-3)
D14.set_attr(h=CPSI('H', 'Q', 0, 'P', 41*1e5, 'water')/1e3)
D16.set_attr(h=CPSI('H', 'Q', 1, 'P', 41*1e5, 'water')/1e3)


#components Data Evaporator nr.2
cmp_pmp2.set_attr(eta_s=0.8)
cmp_eco2.set_attr(pr1=1, pr2=1)
cmp_eco_wp2.set_attr(pr1=1, pr2=1)
cmp_eva2.set_attr(pr1=1)
#data Evaporator nr.2 connections
D21.set_attr(m=100)
D22.set_attr(p=15)
D23.set_attr(Td_bp=-3)
D24.set_attr(h=CPSI('H', 'Q', 0, 'P', 15*1e5, 'water')/1e3)
D26.set_attr(h=CPSI('H', 'Q', 1, 'P', 15*1e5, 'water')/1e3)


#components Data Evaporator nr.3
cmp_pmp3.set_attr(eta_s=0.8)
cmp_eco3.set_attr(pr1=1, pr2=1)
cmp_eco_wp3.set_attr(pr1=1, pr2=1)
cmp_eva3.set_attr(pr1=1)
#data Evaporator nr.3 connections
#D31.set_attr(T=60, p=1, m=250, fluid=water)
D32.set_attr(p=5)
D33.set_attr(Td_bp=-3)
D34.set_attr(h=CPSI('H', 'Q', 0, 'P', 5*1e5, 'water')/1e3)
D36.set_attr(h=CPSI('H', 'Q', 1, 'P', 5*1e5, 'water')/1e3)


#Data Speisewasserbehälter
cmp_pumpe.set_attr(eta_s=0.8)
#Data Speisewasserbehälter Connections
S1.set_attr(m=60, fluid=water)
S2.set_attr(T=60, p=1, m=375, fluid=water)
S3.set_attr(p=4)
S4.set_attr(h=CPSI('H', 'Q', 0, 'P', 4*1e5, 'water')/1e3)

#Data Wärmepumpe Components
cmp_heatsrc.set_attr(pr1=1, pr2=1)
#Data Wärmepumpe Connections
I1.set_attr(m=50, T=250, p=15, fluid=fld_wf)
I5.set_attr(p=3)
I6.set_attr(T=200)



# results
steamgenerator.solve(mode='design')
steamgenerator.print_results()

print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!NEXT!!!!!!!CALCULATION!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

c03.set_attr(m=None)
cmp_eco3.set_attr(ttd_u=25)
cmp_cc.set_attr(lamb=None)
c04.set_attr(T=1600)
S1.set_attr(m=None, h=CPSI('H', 'Q', 1, 'P', 4*1e5, 'water')/1e3)
I6.set_attr(T=None)
cmp_heatsrc.set_attr(ttd_l=25)

steamgenerator.solve(mode='design')
steamgenerator.print_results()

