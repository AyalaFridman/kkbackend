from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controllers import (
    needy_controller,
    fund_controller,
    project_controller,
    allocation_controller,
    special_support_controller,
    support_controller,
    service_provider_controller,
    income_controller,
    account_controller,
    expense_controller,
    child_controller,
    donor_controller,
    upload_controller,
    payments_controller
)

# יצירת יישום FastAPI
app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# רישום כל ה-controllers
app.include_router(needy_controller.router, prefix="/needy", tags=["Needy"])
app.include_router(fund_controller.router, prefix="/fund", tags=["Fund"])
app.include_router(project_controller.router, prefix="/project", tags=["Project"])
app.include_router(
    allocation_controller.router, prefix="/allocation", tags=["Allocation"]
)
app.include_router(
    special_support_controller.router, prefix="/specialSupport", tags=["SpecialSupport"]
)
app.include_router(support_controller.router, prefix="/support", tags=["Support"])
app.include_router(
    service_provider_controller.router,
    prefix="/serviceProvider",
    tags=["ServiceProvider"],
)
app.include_router(income_controller.router, prefix="/income", tags=["Income"])
app.include_router(account_controller.router, prefix="/account", tags=["Account"])
app.include_router(expense_controller.router, prefix="/expense", tags=["Expense"])
app.include_router(child_controller.router, prefix="/child", tags=["Children"])
app.include_router(donor_controller.router, prefix="/donor", tags=["donors"])
app.include_router(upload_controller.router, prefix= "/upload", tags = ["uploads"])
app.include_router(payments_controller.router, prefix= "/payment", tags = ["payments"])


@app.get("/")
def root():
    return {"message": "Welcome to the Needy API!"}
