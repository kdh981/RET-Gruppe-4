from tespy.networks import Network
from tespy.components import (Source, Sink, CombustionChamber, Turbine, Compressor, Drum, HeatExchanger, Pump, SimpleHeatExchanger, Valve, Pipe, Splitter, Merge, CycleCloser)
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

# components of system Steamgenerator nr.1
cmp_eco1 = HeatExchanger('economiser1')
cmp_pmp1 = Pump('pumpe1')
cmp_eva1 = HeatExchanger('evaporator1')
cmp_dr1 = Drum('Trommel1')
cmp_heatex1 = SimpleHeatExchanger('Kunde1',dissipative=False)
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

#Cycle Closer
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
c11 = Connection(cmp_eco3, 'out1', snk_fg, 'in1', label='11')

steamgenerator.add_conns(c01, c02, c03, c04, c05, c06, c07, c08, c09, c10, c11)

#connection Evaporator nr.1 41bar
D11 = Connection(cmp_split3, 'out2', cmp_pmp1, 'in1', label='D11')
D12 = Connection(cmp_pmp1, 'out1', cmp_eco1, 'in2', label='D12')
D13 = Connection(cmp_eco1, 'out2', cmp_dr1, 'in1', label='D13')
D14 = Connection(cmp_dr1, 'out1', cmp_eva1, 'in2', label='D14')
D15 = Connection(cmp_eva1, 'out2', cmp_dr1, 'in2', label='D15')
D16 = Connection(cmp_dr1, 'out2', cmp_heatex1, 'in1', label='D16')
D17 = Connection(cmp_heatex1, 'out1', cmp_merge1, 'in1', label='D17')

steamgenerator.add_conns(D11, D12, D13, D14, D15, D16, D17)

#connection Evaporator nr.2 15bar
D21 = Connection(cmp_split3, 'out1', cmp_pmp2, 'in1', label='D21')
D22 = Connection(cmp_pmp2, 'out1', cmp_eco2, 'in2', label='D22')
D23 = Connection(cmp_eco2, 'out2', cmp_dr2, 'in1', label='D23')
D24 = Connection(cmp_dr2, 'out1', cmp_eva2, 'in2', label='D24')
D25 = Connection(cmp_eva2, 'out2', cmp_dr2, 'in2', label='D25')
D26 = Connection(cmp_dr2, 'out2', cmp_heatex2, 'in1', label='D26')
D27 = Connection(cmp_heatex2, 'out1', cmp_merge1, 'in2', label='D27')

steamgenerator.add_conns(D21, D22, D23, D24, D25, D26, D27)

#connection Evaporator nr.3 5bar
D31 = Connection(cmp_split2, 'out2', cmp_pmp3, 'in1', label='D31')
D32 = Connection(cmp_pmp3, 'out1', cmp_eco3, 'in2', label='D32')
D33 = Connection(cmp_eco3, 'out2', cmp_dr3, 'in1', label='D33')
D34 = Connection(cmp_dr3, 'out1', cmp_eva3, 'in2', label='D34')
D35 = Connection(cmp_eva3, 'out2', cmp_dr3, 'in2', label='D35')
D36 = Connection(cmp_dr3, 'out2', cmp_split1, 'in1', label='D36')
D37 = Connection(cmp_split1, 'out1', cmp_drossel, 'in1', label='D37')
D38 = Connection(cmp_split1, 'out2', cmp_heatex3, 'in1', label='D38')
D39 = Connection(cmp_heatex3, 'out1', cmp_merge2, 'in1', label='D39')

steamgenerator.add_conns(D31, D32, D33, D34, D35, D36, D37, D38, D39)

#Kondensatrückführung
K1 = Connection(cmp_merge1, 'out1', cmp_merge2, 'in2', label='K1')
K2 = Connection(cmp_merge2, 'out1', cmp_entgaser, 'in1', label='K2')
K3 = Connection(cmp_drossel, 'out1', cmp_pipe, 'in1', label='K3')
K4 = Connection(cmp_pipe, 'out1', cmp_entgaser, 'in2', label='K4')
K5 = Connection(cmp_entgaser, 'out1', cyclecloser, 'in1', label='K5')
K6 = Connection(cyclecloser, 'out1', cmp_split2, 'in1', label='K6')
#K5 = Connection(cmp_entgaser, 'out1', cmp_split2, 'in1', label='K5')
K7 = Connection(cmp_split2, 'out1', cmp_split3, 'in1', label='K7')

steamgenerator.add_conns(K1, K2, K3, K4, K5, K6, K7)

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
cmp_eva1.set_attr(pr1=1)
cmp_heatex1.set_attr(pr=1/41)

#data Evaporator nr.1 connections
D11.set_attr(m=25, fluid=water)
D12.set_attr(p=41)
D13.set_attr(h=CPSI('H', 'Q', 0, 'P', 40*1e5, 'water')/1e3)
D15.set_attr(h=CPSI('H', 'Q', 1, 'P', 40*1e5, 'water')/1e3)
#D17.set_attr(p=1)

#components Data Evaporator nr.2
cmp_pmp2.set_attr(eta_s=0.8)
cmp_eco2.set_attr(pr1=1, pr2=1)
cmp_eva2.set_attr(pr1=1)
cmp_heatex2.set_attr(pr=1/15)

#data Evaporator nr.2 connections
D21.set_attr(m=100)
D22.set_attr(p=15)
D23.set_attr(h=CPSI('H', 'Q', 0, 'P', 14*1e5, 'water')/1e3)
D25.set_attr(h=CPSI('H', 'Q', 1, 'P', 14*1e5, 'water')/1e3)
#D27.set_attr(p=1)

#components Data Evaporator nr.3
cmp_pmp3.set_attr(eta_s=0.8)
cmp_eco3.set_attr(pr1=1, pr2=1)
cmp_eva3.set_attr(pr1=1)
cmp_heatex3.set_attr(pr=1/5)

#data Evaporator nr.3 connections
#D31.set_attr()
D32.set_attr(p=5)
D33.set_attr(h=CPSI('H', 'Q', 0, 'P', 4*1e5, 'water')/1e3)
D35.set_attr(h=CPSI('H', 'Q', 1, 'P', 4*1e5, 'water')/1e3)
D38.set_attr(m=250)

#data deaerator
#cmp_pipe.set_attr(pr=1/4)

#deaerator Connection data
K3.set_attr(p=4)
K4.set_attr(p=1)
K2.set_attr(T=60, p=1)
#K5.set_attr(m=401.7)



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
    {'comp': cmp_eva3,'base': 'bus'}
)

#heatConsumer = Bus('total heat input')
#heatConsumer.add_comps(
#    {'comp': cmp_heatex1,'base': 'bus'},
#   {'comp': cmp_heatex2,'base': 'bus'},
#    {'comp': cmp_heatex3,'base': 'bus'}
#)

exergy_loss_bus = Bus('exergy loss')
exergy_loss_bus.add_comps({'comp': src_air, 'base': 'bus'}, {'comp': snk_fg})


steamgenerator.add_busses(power, electricityPW, electricConsumer,heatProducer,exergy_loss_bus)

#exergy analysis
ean = ExergyAnalysis(network=steamgenerator, E_F=[power, electricConsumer], E_P=[electricityPW, heatProducer], E_L=[exergy_loss_bus])
ean.analyse(1.013, 25)
ean.print_results()

