# ex: set ro:
# DO NOT EDIT.
# generated by smc (http://smc.sourceforge.net/)
# from file : version2.sm

import statemap


class AppClassState(statemap.State):

    def Entry(self, fsm):
        pass

    def Exit(self, fsm):
        pass

    def Colom(self, fsm):
        self.Default(fsm)

    def Digit(self, fsm, letter):
        self.Default(fsm)

    def Dot(self, fsm, letter):
        self.Default(fsm)

    def EOS(self, fsm):
        self.Default(fsm)

    def Letter(self, fsm, letter):
        self.Default(fsm)

    def Space(self, fsm):
        self.Default(fsm)

    def TargetName_1(self, fsm):
        self.Default(fsm)

    def UnderLine(self, fsm, letter):
        self.Default(fsm)

    def Unknown(self, fsm):
        self.Default(fsm)

    def Default(self, fsm):
        msg = "\n\tState: %s\n\tTransition: %s" % (
            fsm.getState().getName(), fsm.getTransition())
        raise statemap.TransitionUndefinedException(msg)

class Map1_Default(AppClassState):

    def Letter(self, fsm, letter):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.Unacceptable()
        finally:
            fsm.setState(Map1.Error)
            fsm.getState().Entry(fsm)


    def Digit(self, fsm, letter):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.Unacceptable()
        finally:
            fsm.setState(Map1.Error)
            fsm.getState().Entry(fsm)


    def Colom(self, fsm):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.Unacceptable()
        finally:
            fsm.setState(Map1.Error)
            fsm.getState().Entry(fsm)


    def Dot(self, fsm, letter):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.Unacceptable()
        finally:
            fsm.setState(Map1.Error)
            fsm.getState().Entry(fsm)


    def UnderLine(self, fsm, letter):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.Unacceptable()
        finally:
            fsm.setState(Map1.Error)
            fsm.getState().Entry(fsm)


    def Unknown(self, fsm):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.Unacceptable()
        finally:
            fsm.setState(Map1.Error)
            fsm.getState().Entry(fsm)


    def EOS(self, fsm):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.Unacceptable()
        finally:
            fsm.setState(Map1.Error)
            fsm.getState().Entry(fsm)


    def Space(self, fsm):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.Unacceptable()
        finally:
            fsm.setState(Map1.Error)
            fsm.getState().Entry(fsm)


    def TargetName_1(self, fsm):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.Clear()
        finally:
            fsm.setState(Map1.TargetName_1)
            fsm.getState().Entry(fsm)


class Map1_TargetName_1(Map1_Default):

    def Dot(self, fsm, letter):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.AddToName(letter)
            ctxt.counterInc()
        finally:
            fsm.setState(Map1.TargetName_2)
            fsm.getState().Entry(fsm)


    def Letter(self, fsm, letter):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.AddToName(letter)
            ctxt.counterInc()
        finally:
            fsm.setState(Map1.TargetName_2)
            fsm.getState().Entry(fsm)


    def UnderLine(self, fsm, letter):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.AddToName(letter)
            ctxt.counterInc()
        finally:
            fsm.setState(Map1.TargetName_2)
            fsm.getState().Entry(fsm)


class Map1_TargetName_2(Map1_Default):

    def Colom(self, fsm):
        ctxt = fsm.getOwner()
        if ctxt.GetNonFirstSymbol() :
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt.SetTargetName()
            finally:
                fsm.setState(Map1.TN_In_List_1)
                fsm.getState().Entry(fsm)
        else:
            Map1_Default.Colom(self, fsm)
        
    def Digit(self, fsm, letter):
        ctxt = fsm.getOwner()
        endState = fsm.getState()
        fsm.clearState()
        try:
            ctxt.AddToName(letter)
            ctxt.counterInc()
        finally:
            fsm.setState(endState)


    def Dot(self, fsm, letter):
        ctxt = fsm.getOwner()
        endState = fsm.getState()
        fsm.clearState()
        try:
            ctxt.AddToName(letter)
            ctxt.counterInc()
        finally:
            fsm.setState(endState)


    def Letter(self, fsm, letter):
        ctxt = fsm.getOwner()
        endState = fsm.getState()
        fsm.clearState()
        try:
            ctxt.AddToName(letter)
            ctxt.counterInc()
        finally:
            fsm.setState(endState)


    def UnderLine(self, fsm, letter):
        ctxt = fsm.getOwner()
        endState = fsm.getState()
        fsm.clearState()
        try:
            ctxt.AddToName(letter)
            ctxt.counterInc()
        finally:
            fsm.setState(endState)


class Map1_TN_In_List_1(Map1_Default):

    def Dot(self, fsm, letter):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.AddToName(letter)
            ctxt.counterInc()
        finally:
            fsm.setState(Map1.TN_In_List_2)
            fsm.getState().Entry(fsm)


    def EOS(self, fsm):
        ctxt = fsm.getOwner()
        if ctxt.NonZero() :
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt.AddToTNList()
                ctxt.Acceptable()
            finally:
                fsm.setState(Map1.OK)
                fsm.getState().Entry(fsm)
        else:
            Map1_Default.EOS(self, fsm)
        
    def Letter(self, fsm, letter):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.AddToName(letter)
            ctxt.counterInc()
        finally:
            fsm.setState(Map1.TN_In_List_2)
            fsm.getState().Entry(fsm)


    def Space(self, fsm):
        ctxt = fsm.getOwner()
        if ctxt.Zero() :
            # No actions.
            pass
        else:
            Map1_Default.Space(self, fsm)
        
    def UnderLine(self, fsm, letter):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.AddToName(letter)
            ctxt.counterInc()
        finally:
            fsm.setState(Map1.TN_In_List_2)
            fsm.getState().Entry(fsm)


class Map1_TN_In_List_2(Map1_Default):

    def Digit(self, fsm, letter):
        ctxt = fsm.getOwner()
        endState = fsm.getState()
        fsm.clearState()
        try:
            ctxt.AddToName(letter)
            ctxt.counterInc()
        finally:
            fsm.setState(endState)


    def Dot(self, fsm, letter):
        ctxt = fsm.getOwner()
        endState = fsm.getState()
        fsm.clearState()
        try:
            ctxt.AddToName(letter)
            ctxt.counterInc()
        finally:
            fsm.setState(endState)


    def EOS(self, fsm):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.AddToTNList()
            ctxt.Acceptable()
        finally:
            fsm.setState(Map1.OK)
            fsm.getState().Entry(fsm)


    def Letter(self, fsm, letter):
        ctxt = fsm.getOwner()
        endState = fsm.getState()
        fsm.clearState()
        try:
            ctxt.AddToName(letter)
            ctxt.counterInc()
        finally:
            fsm.setState(endState)


    def Space(self, fsm):
        ctxt = fsm.getOwner()
        fsm.getState().Exit(fsm)
        fsm.clearState()
        try:
            ctxt.AddToTNList()
        finally:
            fsm.setState(Map1.TN_In_List_1)
            fsm.getState().Entry(fsm)


    def UnderLine(self, fsm, letter):
        ctxt = fsm.getOwner()
        endState = fsm.getState()
        fsm.clearState()
        try:
            ctxt.AddToName(letter)
            ctxt.counterInc()
        finally:
            fsm.setState(endState)


class Map1_OK(Map1_Default):
    pass

class Map1_Error(Map1_Default):
    pass

class Map1(object):

    TargetName_1 = Map1_TargetName_1('Map1.TargetName_1', 0)
    TargetName_2 = Map1_TargetName_2('Map1.TargetName_2', 1)
    TN_In_List_1 = Map1_TN_In_List_1('Map1.TN_In_List_1', 2)
    TN_In_List_2 = Map1_TN_In_List_2('Map1.TN_In_List_2', 3)
    OK = Map1_OK('Map1.OK', 4)
    Error = Map1_Error('Map1.Error', 5)
    Default = Map1_Default('Map1.Default', -1)

class AppClass_sm(statemap.FSMContext):

    def __init__(self, owner):
        statemap.FSMContext.__init__(self, Map1.TargetName_1)
        self._owner = owner

    def __getattr__(self, attrib):
        def trans_sm(*arglist):
            self._transition = attrib
            getattr(self.getState(), attrib)(self, *arglist)
            self._transition = None
        return trans_sm

    def enterStartState(self):
        self._state.Entry(self)

    def getOwner(self):
        return self._owner

# Local variables:
#  buffer-read-only: t
# End:
