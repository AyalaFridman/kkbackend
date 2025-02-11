from models.donation_keva_schema import DonationsKevaSchema
from models.donor_schema import DonorSchema

class DonationsKevaSchemaGet(DonationsKevaSchema):
    id : int
    donor: DonorSchema  
    class Config:
        from_attributes = True