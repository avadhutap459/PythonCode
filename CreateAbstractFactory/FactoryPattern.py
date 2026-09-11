from abc import ABC , abstractmethod

class IPremium:
    
    def __init__(self,PT , PPT):
        self.PT = PT
        self.PPT = PPT
        
    @abstractmethod
    def calpremium(self):
        pass

class IProposal:
    def __init__(self,ProposalDetail ):
        self.ProposalDetail = ProposalDetail
        
    @abstractmethod
    def calproposal(self):
        pass

class Premium(IPremium):
    def __init__(self, PT, PPT):
        super().__init__(PT, PPT)
    
    def calpremium(self):
        print("Calculate premium on following parameter : " , self.PT , "and " , self.PPT)

class Proposal(IProposal):
    def __init__(self, ProposalDetail):
        super().__init__(ProposalDetail)
    
    def calproposal(self):
        print("Calculate proposal on following parameter : " , self.ProposalDetail )


class BackFactory:
    @abstractmethod
    def FProposal(self, ProposalDetail):
        pass
    
    @abstractmethod
    def FPremium(self,PT , PPT):
        pass

class BOIFactory(BackFactory):
    def FProposal(self, ProposalDetail):
        return Proposal(ProposalDetail)
    
    def FPremium(self, PT, PPT):
        return Premium(PT , PPT)

class UBIFactory(BackFactory):
    def FProposal(self, ProposalDetail):
        return Proposal(ProposalDetail)
        
    def FPremium(self, PT, PPT):
        return Premium(PT , PPT)
    

if __name__ == "__main__":
    boi_factory = BOIFactory()
    ubi_factory = UBIFactory()
    
    calpremium  = boi_factory.FPremium(2 , 25)
    calproposal = boi_factory.FProposal("Avadhut")
    
    calpremium.calpremium()
    calproposal.calproposal();