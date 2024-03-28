from tespy.networks import Network
from tespy.components import (Source, Sink, CombustionChamber, Turbine, Compressor, Drum, HeatExchanger, Pump, SimpleHeatExchanger, Valve, Pipe, Splitter, Merge, ParabolicTrough, CycleCloser)
from tespy.connections import Connection, Bus, Ref
from CoolProp.CoolProp import PropsSI as CPSI
from tespy.tools import ExergyAnalysis

# fluids
water = {'H2O': 1}
fld_air = {'O2': 0.21, 'N2': 0.79}
fld_gas = {'CH4': 1}
oel = {'INCOMP::S800': 1}

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
cmp_heatex1 = SimpleHeatExchanger('Kunde1', dissipative=False)
#cmp_merge1 = Merge('zuführung')
src_H2O = Source('water1')
snk_H20 = Sink('steam1')

# components of system Steamgenerator nr.2
cmp_eco2 = HeatExchanger('economiser2')
cmp_pmp2 = Pump('pumpe2')
cmp_eva2 = HeatExchanger('evaporator2')
cmp_dr2 = Drum('Trommel2')
cmp_heatex2 = SimpleHeatExchanger('Kunde2', dissipative=False)
cmp_merge1 = Merge('zuführung1')
src2_H2O = Source('water2')
snk2_H20 = Sink('steam2')

# components of system Steamgenerator nr.3
cmp_eco3 = HeatExchanger('economiser3')
cmp_pmp3 = Pump('pumpe3')
cmp_eva3 = HeatExchanger('evaporator3')
cmp_dr3 = Drum('Trommel3')
cmp_heatex3 = SimpleHeatExchanger('Kunde3', dissipative=False)
cmp_merge2 = Merge('zuführung2')
cmp_drossel = Valve('drossel')
cmp_split1 = Splitter('dampftrennung')
src3_H2O = Source('water3')
snk3_H20 = Sink('steam3')

#Speisewasserbehälter + Entgaser
cmp_entgaser = Merge('Entgaser')
cmp_pipe = Pipe('Dampf zugabe')
cmp_split2 = Splitter('Massentrennung1')
cmp_split3 = Splitter('Massentrennung2')

#Solar
cmp_pt = ParabolicTrough('Solar')
cmp_sl_eco1 = HeatExchanger('vorwärmer1')
cmp_sl_eco2 = HeatExchanger('vorwärmer2')
cmp_sl_eco3 = HeatExchanger('vorwärmer3')

#Cycle Closer
cyclecloser1 = CycleCloser('CycleCloser1')
cyclecloser2 = CycleCloser('CycleCloser2')

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
c11 = Connection(cmp_eco3, 'out1', snk_fg, 'in1', label='11')

steamgenerator.add_conns(c01, c02, c03, c04, c05, c06, c07, c08, c09, c10, c11)

#connection Evaporator nr.1 41bar
D101 = Connection(cmp_split3, 'out2', cmp_pmp1, 'in1', label='D101')
D102 = Connection(cmp_pmp1, 'out1', cmp_sl_eco1, 'in2', label='D102')
D103 = Connection(cmp_sl_eco1, 'out2', cmp_eco1, 'in2', label='D103')
D104 = Connection(cmp_eco1, 'out2', cmp_dr1, 'in1', label='D104')
D105 = Connection(cmp_dr1, 'out1', cmp_eva1, 'in2', label='D105')
D106 = Connection(cmp_eva1, 'out2', cmp_dr1, 'in2', label='D106')
D107 = Connection(cmp_dr1, 'out2', cmp_heatex1, 'in1', label='D107')
D108 = Connection(cmp_heatex1, 'out1', cmp_merge1, 'in1', label='D108')

steamgenerator.add_conns(D101, D102, D103, D104, D105, D106, D107, D108)

#connection Evaporator nr.2 15bar
D201 = Connection(cmp_split3, 'out1', cmp_pmp2, 'in1', label='D201')
D202 = Connection(cmp_pmp2, 'out1', cmp_sl_eco2, 'in2', label='D202')
D203 = Connection(cmp_sl_eco2, 'out2', cmp_eco2, 'in2', label='D203')
D204 = Connection(cmp_eco2, 'out2', cmp_dr2, 'in1', label='D204')
D205 = Connection(cmp_dr2, 'out1', cmp_eva2, 'in2', label='D205')
D206 = Connection(cmp_eva2, 'out2', cmp_dr2, 'in2', label='D206')
D207 = Connection(cmp_dr2, 'out2', cmp_heatex2, 'in1', label='D207')
D208 = Connection(cmp_heatex2, 'out1', cmp_merge1, 'in2', label='D208')

steamgenerator.add_conns(D201, D202, D203, D204, D205, D206, D207, D208)

#connection Evaporator nr.3 5bar
D301 = Connection(cmp_split2, 'out2', cmp_pmp3, 'in1', label='D301')
D302 = Connection(cmp_pmp3, 'out1', cmp_sl_eco3, 'in2', label='D302')
D303 = Connection(cmp_sl_eco3, 'out2', cmp_eco3, 'in2', label='D303')
D304 = Connection(cmp_eco3, 'out2', cmp_dr3, 'in1', label='D304')
D305 = Connection(cmp_dr3, 'out1', cmp_eva3, 'in2', label='D305')
D306 = Connection(cmp_eva3, 'out2', cmp_dr3, 'in2', label='D306')
D307 = Connection(cmp_dr3, 'out2', cmp_split1, 'in1', label='D307')
D308 = Connection(cmp_split1, 'out1', cmp_drossel, 'in1', label='D308')
D309 = Connection(cmp_split1, 'out2', cmp_heatex3, 'in1', label='D309')
D310 = Connection(cmp_heatex3, 'out1', cmp_merge2, 'in1', label='D310')

steamgenerator.add_conns(D301, D302, D303, D304, D305, D306, D307, D308, D309, D310)

#Kondensatrückführung
K1 = Connection(cmp_merge1, 'out1', cmp_merge2, 'in2', label='K1')
K2 = Connection(cmp_merge2, 'out1', cmp_entgaser, 'in1', label='K2')
K3 = Connection(cmp_drossel, 'out1', cmp_pipe, 'in1', label='K3')
K4 = Connection(cmp_pipe, 'out1', cmp_entgaser, 'in2', label='K4')
K5 = Connection(cmp_entgaser, 'out1', cyclecloser1, 'in1', label='K5')
K6 = Connection(cyclecloser1, 'out1', cmp_split2, 'in1', label='K6')
#K5 = Connection(cmp_entgaser, 'out1', cmp_split2, 'in1', label='K5')
K7 = Connection(cmp_split2, 'out1', cmp_split3, 'in1', label='K7')

steamgenerator.add_conns(K1, K2, K3, K4, K5, K6, K7)

#Solar Cycle
Scc = Connection(cyclecloser2, 'out1', cmp_pt, 'in1', label='S1')
S1 = Connection(cmp_pt, 'out1', cmp_sl_eco1, 'in1', label='S2')
S2 = Connection(cmp_sl_eco1, 'out1', cmp_sl_eco2, 'in1', label='S3')
S3 = Connection(cmp_sl_eco2, 'out1', cmp_sl_eco3, 'in1', label='S4')
S4 = Connection(cmp_sl_eco3, 'out1', cyclecloser2, 'in1', label='S5')

steamgenerator.add_conns(S1, S2, S3, S4, Scc)

# components Data Turbine System
cmp_cp.set_attr(eta_s=0.8)
cmp_tb.set_attr(eta_s=0.9)
cmp_cc.set_attr(lamb=2.5)

#data Turbine connections
c01.set_attr(p=1, T=15, fluid=fld_air)
c03.set_attr(T=15, m=69, p=30, fluid=fld_gas)
c11.set_attr(p=1)

#components Data Evaporator nr.1
cmp_pmp1.set_attr(eta_s=0.8)
cmp_eco1.set_attr(pr1=1, pr2=1)
cmp_sl_eco1.set_attr(pr1=1, pr2=1)
cmp_eva1.set_attr(pr1=1)
#cmp_heatex1.set_attr(pr=1/41)

#data Evaporator nr.1 connections
D101.set_attr(m=25, fluid=water)
D102.set_attr(p=41)
D104.set_attr(h=CPSI('H', 'Q', 0, 'P', 40*1e5, 'water')/1e3)
D106.set_attr(h=CPSI('H', 'Q', 1, 'P', 40*1e5, 'water')/1e3)
D108.set_attr(p=1)

#components Data Evaporator nr.2
cmp_pmp2.set_attr(eta_s=0.8)
cmp_eco2.set_attr(pr1=1, pr2=1)
cmp_sl_eco2.set_attr(pr1=1, pr2=1)
cmp_eva2.set_attr(pr1=1)
#cmp_heatex2.set_attr(pr=1/15)

#data Evaporator nr.2 connections
D201.set_attr(m=100)
D202.set_attr(p=15)
D203.set_attr(h=CPSI('H', 'Q', 0, 'P', 14*1e5, 'water')/1e3)
D206.set_attr(h=CPSI('H', 'Q', 1, 'P', 14*1e5, 'water')/1e3)
D208.set_attr(p=1)

#components Data Evaporator nr.3
cmp_pmp3.set_attr(eta_s=0.8)
cmp_eco3.set_attr(pr1=1, pr2=1)
cmp_sl_eco3.set_attr(pr1=1, pr2=1)
cmp_eva3.set_attr(pr1=1)
#cmp_heatex3.set_attr(pr=1/5)

#data Evaporator nr.3 connections
D302.set_attr(p=5)
D304.set_attr(h=CPSI('H', 'Q', 0, 'P', 4*1e5, 'water')/1e3)
D306.set_attr(h=CPSI('H', 'Q', 1, 'P', 4*1e5, 'water')/1e3)
D309.set_attr(m=250)

#data deaerator
#cmp_pipe.set_attr(pr=1/4)

#deaerator Connection data
K3.set_attr(p=4)
K4.set_attr(p=1)
K2.set_attr(T=60, p=1)
K5.set_attr(m=401.7)
#
#Solar Data
cmp_tb.set_attr(pr=1)

#Solar data connection
S1.set_attr(T=300, p=10, m=138.9, fluid=oel)
S4.set_attr(T=100)

# results
steamgenerator.solve(mode='design')
steamgenerator.print_results()

#print('Nächste Rechnung !!!!')

#c03.set_attr(m=None)
#cmp_eco1.set_attr(ttd_l=20)

#steamgenerator.solve(mode='design')
#steamgenerator.print_results()

#print('Nächste Rechnung !!!!')
#
#c01.set_attr(m=None)
#c04.set_attr(T=1600)
#
#steamgenerator.solve(mode='design')
#steamgenerator.print_results()

#EXERGIE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

power = Bus('total input Power')
power.add_comps(
    {'comp': cmp_cc, 'base': 'bus'}
)

electricityPW = Bus('total output electric Power')
electricityPW.add_comps(
    {'comp': cmp_tb, 'char': 0.985,'base': 'bus'}
)

electricConsumer = Bus('total input electric Power')
electricConsumer.add_comps(
    {'comp': cmp_pmp1, 'char': 0.975, 'base': 'bus'},
    {'comp': cmp_pmp2, 'char': 0.975, 'base': 'bus'},
    {'comp': cmp_pmp3, 'char': 0.975, 'base': 'bus'}
)

heatProducer = Bus('total heat output')
heatProducer.add_comps(
    {'comp': cmp_eco1,'base': 'bus'},
    {'comp': cmp_eco2,'base': 'bus'},
    {'comp': cmp_eco3,'base': 'bus'},
    {'comp': cmp_eva1,'base': 'bus'},
    {'comp': cmp_eva2,'base': 'bus'},
    {'comp': cmp_eva3,'base': 'bus'},
    {'comp': cmp_sl_eco1,'base': 'bus'},
    {'comp': cmp_sl_eco2,'base': 'bus'},
    {'comp': cmp_sl_eco3,'base': 'bus'}
)

#heatConsumer = Bus('total heat input')
#heatConsumer.add_comps(
#    {'comp': cmp_heatex1,'base': 'bus'},
#   {'comp': cmp_heatex2,'base': 'bus'},
#    {'comp': cmp_heatex3,'base': 'bus'}
#)

sunpower = Bus('Solar power')
sunpower.add_comps(
    {'comp': cmp_pt, 'base': 'bus'}
)

exergy_loss_bus = Bus('exergy loss')
exergy_loss_bus.add_comps({'comp': src_air, 'base': 'bus'}, {'comp': snk_fg})


steamgenerator.add_busses(power, electricityPW, electricConsumer,heatProducer,exergy_loss_bus)

#exergy analysis
ean = ExergyAnalysis(network=steamgenerator, E_F=[power, electricConsumer, sunpower], E_P=[electricityPW, heatProducer], E_L=[exergy_loss_bus])
ean.analyse(1.013, 25)
ean.print_results()
