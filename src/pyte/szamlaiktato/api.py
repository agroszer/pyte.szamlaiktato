import builtins
from typing import Any, Optional
from dataclasses import dataclass, asdict
from .client import OnlineSzamlazoClient


@dataclass
class InstallRequest:
    user: str
    service_key: str
    block_name: str
    name: str
    country: str
    postcode: str
    city: str
    street: str
    tax_number: str
    bank_name: str
    bank_number: str
    invoice_number_pre: str
    invoice_number_length: int
    email: str
    invoice_issue: int
    restart_number_by_year: int
    street_number: Optional[str] = None
    door: Optional[str] = None
    eu_tax_number: Optional[str] = None
    telephone: Optional[str] = None
    comment: Optional[str] = None
    lang: Optional[str] = None
    logo: Optional[Any] = None
    invoice_template: Optional[str] = None
    invoice_number_format: Optional[str] = None
    currency: Optional[str] = None
    installType: Optional[str] = None
    other: Optional[str] = None
    invoice_start: Optional[int] = None
    invoice_mails: Optional[int] = None
    invoice_mails_accounting: Optional[int] = None
    invoice_pdf_mail: Optional[int] = None
    invoice_pay_notice_mails: Optional[int] = None
    pdfProformGeneratePdf: Optional[int] = None
    pdfProformGeneratePdfSend: Optional[int] = None
    invoiceAppearance_paper: Optional[int] = None
    invoiceAppearance_edi: Optional[int] = None
    prepayment_invoice_enabled: Optional[int] = None
    reversevat_invoice_enabled: Optional[int] = None
    cashaccounting_invoice_enabled: Optional[int] = None
    smallBusinessIndicator: Optional[int] = None
    pdfHideCurrencyRate: Optional[int] = None
    bankPairingAutomaticInvoice: Optional[int] = None
    invoiceTax_EU_OSS: Optional[int] = None
    invoice_en16931_xml_attached: Optional[int] = None
    invoiceDigitalSignature: Optional[int] = None
    admin_user_type: Optional[int] = None


@dataclass
class InstallResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    other: Optional[str] = None


@dataclass
class UpdateRequest:
    user: str
    block_name: str
    name: str
    country: str
    postcode: str
    city: str
    street: str
    tax_number: str
    bank_name: str
    bank_number: str
    email: str
    invoice_issue: int
    restart_number_by_year: int
    street_number: Optional[str] = None
    door: Optional[str] = None
    eu_tax_number: Optional[str] = None
    telephone: Optional[str] = None
    comment: Optional[str] = None
    lang: Optional[str] = None
    logo: Optional[Any] = None
    invoice_template: Optional[str] = None
    other: Optional[str] = None
    invoice_start: Optional[int] = None
    invoice_mails: Optional[int] = None
    invoice_mails_accounting: Optional[int] = None
    invoice_pdf_mail: Optional[int] = None
    invoice_pay_notice_mails: Optional[int] = None
    pdfProformGeneratePdf: Optional[int] = None
    pdfProformGeneratePdfSend: Optional[int] = None
    invoiceAppearance_paper: Optional[int] = None
    invoiceAppearance_edi: Optional[int] = None
    prepayment_invoice_enabled: Optional[int] = None
    reversevat_invoice_enabled: Optional[int] = None
    cashaccounting_invoice_enabled: Optional[int] = None
    smallBusinessIndicator: Optional[int] = None
    pdfHideCurrencyRate: Optional[int] = None
    bankPairingAutomaticInvoice: Optional[int] = None
    invoiceTax_EU_OSS: Optional[int] = None
    invoice_en16931_xml_attached: Optional[int] = None
    invoiceDigitalSignature: Optional[int] = None
    admin_user_type: Optional[int] = None


@dataclass
class UpdateResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    other: Optional[str] = None


@dataclass
class CustomerAddRequest:
    sid: str
    name: str
    country: str
    postcode: str
    city: str
    street: str
    email: str
    invoice_send: int
    active: int
    lang: str
    legal_status: int
    region: Optional[str] = None
    street_number: Optional[str] = None
    door: Optional[str] = None
    tax_number: Optional[str] = None
    group_tax_number: Optional[str] = None
    eu_tax_number: Optional[str] = None
    comment: Optional[str] = None
    phone: Optional[str] = None
    bank_name: Optional[str] = None
    bank: Optional[str] = None
    firm_type: Optional[int] = None
    other: Optional[str] = None


@dataclass
class CustomerAddResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    sid: Optional[str] = None


@dataclass
class CustomerModifyRequest:
    sid: str
    name: str
    country: str
    postcode: str
    city: str
    street: str
    active: int
    lang: str
    firm_type: int
    legal_status: str
    region: Optional[str] = None
    street_number: Optional[str] = None
    door: Optional[str] = None
    tax_number: Optional[str] = None
    group_tax_number: Optional[str] = None
    eu_tax_number: Optional[str] = None
    email: Optional[str] = None
    invoice_send: Optional[int] = None
    comment: Optional[str] = None
    phone: Optional[str] = None
    bank_name: Optional[str] = None
    bank: Optional[str] = None
    other: Optional[str] = None


@dataclass
class CustomerModifyResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    sid: Optional[str] = None


@dataclass
class CustomerGetRequest:
    sid: str
    tax_number: Optional[str] = None
    email: Optional[str] = None


@dataclass
class CustomerGetResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    sid: Optional[str] = None
    name: Optional[str] = None
    country: Optional[str] = None
    region: Optional[str] = None
    postcode: Optional[str] = None
    city: Optional[str] = None
    street: Optional[str] = None
    street_number: Optional[str] = None
    door: Optional[str] = None
    tax_number: Optional[str] = None
    group_tax_number: Optional[str] = None
    eu_tax_number: Optional[str] = None
    email: Optional[str] = None
    invoice_send: Optional[int] = None
    comment: Optional[str] = None
    phone: Optional[str] = None
    bank_name: Optional[str] = None
    bank: Optional[str] = None
    active: Optional[int] = None
    lang: Optional[str] = None
    firm_type: Optional[int] = None
    legal_status: Optional[str] = None
    date: Optional[str] = None
    users_id: Optional[int] = None
    master_customer_sid: Optional[str] = None
    modify_date: Optional[str] = None
    other_json: Optional[str] = None


@dataclass
class CustomerActivateRequest:
    sid: str


@dataclass
class CustomerActivateResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    sid: Optional[str] = None


@dataclass
class CustomerInactivateRequest:
    sid: str


@dataclass
class CustomerInactivateResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    sid: Optional[str] = None


@dataclass
class CustomerSwapRequest:
    sid: str
    swapped_sids: builtins.list[builtins.dict[str, Any]]


@dataclass
class CustomerSwapResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    sid: Optional[str] = None


@dataclass
class CustomerListRequest:
    firm_type: Optional[int] = None
    name: Optional[str] = None
    email: Optional[str] = None
    sid: Optional[str] = None
    limit: Optional[int] = None
    page: Optional[int] = None


@dataclass
class CustomerListResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    customers: Optional[builtins.list[builtins.dict[str, Any]]] = None
    sid: Optional[str] = None
    name: Optional[str] = None
    country: Optional[str] = None
    region: Optional[str] = None
    postcode: Optional[str] = None
    city: Optional[str] = None
    street: Optional[str] = None
    street_number: Optional[str] = None
    door: Optional[str] = None
    tax_number: Optional[str] = None
    group_tax_number: Optional[str] = None
    eu_tax_number: Optional[str] = None
    email: Optional[str] = None
    invoice_send: Optional[int] = None
    comment: Optional[str] = None
    phone: Optional[str] = None
    bank: Optional[str] = None
    active: Optional[int] = None
    lang: Optional[str] = None
    legal_status: Optional[str] = None
    date: Optional[str] = None
    users_id: Optional[int] = None
    other_json: Optional[str] = None
    modify_date: Optional[str] = None


@dataclass
class ProductAddRequest:
    sid: str
    name: str
    net_price_single: float
    tax_code: str
    currency: str
    service_id: Optional[str] = None
    comment: Optional[str] = None
    cost_type: Optional[str] = None
    cost_centre: Optional[str] = None
    lang: Optional[builtins.list[builtins.dict[str, Any]]] = None
    short_description: Optional[str] = None
    description: Optional[str] = None
    other: Optional[str] = None
    lineNatureIndicator: Optional[str] = None
    FINAL_DATADELETE_CODE_SET: Optional[int] = None
    intermediatedService: Optional[int] = None


@dataclass
class ProductAddResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    sid: Optional[str] = None


@dataclass
class ProductModifyRequest:
    sid: str
    name: str
    net_price_single: float
    tax_code: str
    currency: str
    service_id: Optional[str] = None
    comment: Optional[str] = None
    cost_type: Optional[str] = None
    cost_centre: Optional[str] = None
    lang: Optional[builtins.list[builtins.dict[str, Any]]] = None
    short_description: Optional[str] = None
    description: Optional[str] = None
    other: Optional[str] = None
    lineNatureIndicator: Optional[str] = None
    FINAL_DATADELETE_CODE_SET: Optional[int] = None
    intermediatedService: Optional[int] = None


@dataclass
class ProductModifyResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    sid: Optional[str] = None


@dataclass
class ProductGetRequest:
    sid: str


@dataclass
class ProductGetResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    sid: Optional[str] = None
    name: Optional[str] = None
    net_price_single: Optional[float] = None
    tax: Optional[str] = None
    currency: Optional[str] = None
    service_id: Optional[str] = None
    comment: Optional[str] = None
    cost_type: Optional[str] = None
    cost_centre: Optional[str] = None
    active: Optional[int] = None
    date: Optional[str] = None
    short_description: Optional[str] = None
    description: Optional[str] = None
    other: Optional[str] = None
    tax_code: Optional[str] = None
    lang: Optional[builtins.list[builtins.dict[str, Any]]] = None
    files_number: Optional[int] = None
    modify_date: Optional[str] = None


@dataclass
class ProductActivateRequest:
    sid: str


@dataclass
class ProductActivateResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    sid: Optional[str] = None


@dataclass
class ProductInactivateRequest:
    sid: str


@dataclass
class ProductInactivateResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    sid: Optional[str] = None


@dataclass
class ProductListRequest:
    cost_type: Optional[str] = None
    cost_centre: Optional[str] = None
    active: Optional[int] = None
    currency: Optional[str] = None
    lang: Optional[str] = None
    name: Optional[str] = None
    sid: Optional[str] = None
    limit: Optional[int] = None
    page: Optional[int] = None


@dataclass
class ProductListResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    numberOfResults: Optional[int] = None
    numberOfPages: Optional[int] = None
    list: Optional[builtins.list[builtins.dict[str, Any]]] = None
    id: Optional[int] = None
    sid: Optional[str] = None
    name: Optional[str] = None
    service_id: Optional[str] = None
    net_price_single: Optional[float] = None
    tax: Optional[float] = None
    tax_categories_id: Optional[int] = None
    tax_code: Optional[str] = None
    currency: Optional[str] = None
    currency_id: Optional[int] = None
    comment: Optional[str] = None
    cost_type: Optional[str] = None
    cost_type_id: Optional[int] = None
    cost_centre: Optional[str] = None
    cost_centre_id: Optional[int] = None
    active: Optional[int] = None
    date: Optional[str] = None
    short_description: Optional[str] = None
    description: Optional[str] = None
    other: Optional[str] = None
    other_json: Optional[str] = None
    orderby: Optional[int] = None
    files_number: Optional[int] = None
    modify_date: Optional[str] = None


@dataclass
class ProductFileListRequest:
    sid: str
    with_file_content: bool


@dataclass
class ProductFileListResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    list: Optional[builtins.list[builtins.dict[str, Any]]] = None
    sid: Optional[str] = None
    filename: Optional[str] = None
    checksum: Optional[str] = None
    file_type: Optional[str] = None
    file: Optional[str] = None


@dataclass
class OuterDatasourcesRequest:
    pass


@dataclass
class OuterDatasourcesResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    list: Optional[builtins.list[builtins.dict[str, Any]]] = None
    id: Optional[int] = None
    name: Optional[str] = None
    code: Optional[str] = None
    description: Optional[str] = None
    settings: Optional[str] = None


@dataclass
class OuterDatasourcesGetRequest:
    type: str


@dataclass
class OuterDatasourcesGetResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    data: Optional[str] = None


@dataclass
class OuterDatasourcesSaveRequest:
    type: str
    data: str
    nav_xml_user: str
    nav_xml_password: str
    nav_xml_key: str
    nav_xml_exchange_key: str
    nav_invoice_download: int


@dataclass
class OuterDatasourcesSaveResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None


@dataclass
class AdminUserAddRequest:
    name: str
    email: str
    mailsend: bool
    groups_id: int
    user_type: int
    service_key: Optional[str] = None


@dataclass
class AdminUserAddResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    sid: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None


@dataclass
class AdminUserPasswordRequest:
    email: str
    new_password: str


@dataclass
class AdminUserPasswordResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    email: Optional[str] = None


@dataclass
class AdminUserDelRequest:
    email: str


@dataclass
class AdminUserDelResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    email: Optional[str] = None


@dataclass
class BlockAddRequest:
    block_name: str
    bank_number: str
    invoice_number_pre: str
    invoice_number_length: int
    invoice_issue: int
    email: str
    restart_number_by_year: int
    lang: str
    invoice_template: str
    currency: str
    other: builtins.list[builtins.dict[str, Any]]
    countryMustVisibleInInvoice: int
    bank_name: Optional[str] = None
    comment: Optional[str] = None
    logo: Optional[int] = None
    invoice_number_format: Optional[str] = None
    invoice_start: Optional[int] = None
    invoice_mails: Optional[int] = None
    invoice_mails_accounting: Optional[int] = None
    invoice_pdf_mail: Optional[int] = None
    invoice_pay_notice_mails: Optional[int] = None
    pdfProformGeneratePdf: Optional[int] = None
    pdfProformGeneratePdfSend: Optional[int] = None
    invoiceAppearance_paper: Optional[int] = None
    invoiceAppearance_edi: Optional[int] = None
    prepayment_invoice_enabled: Optional[int] = None
    reversevat_invoice_enabled: Optional[int] = None
    cashaccounting_invoice_enabled: Optional[int] = None
    smallBusinessIndicator: Optional[int] = None
    pdfHideCurrencyRate: Optional[int] = None
    bankPairingAutomaticInvoice: Optional[int] = None
    invoiceTax_EU_OSS: Optional[int] = None
    invoice_en16931_xml_attached: Optional[int] = None
    invoiceDigitalSignature: Optional[int] = None
    certificate_logo_visible: Optional[int] = None
    order_number_visible: Optional[int] = None
    pdfConvertZpl: Optional[int] = None
    pdfConvertZplDownload: Optional[int] = None
    pdf_design05: Optional[builtins.list[builtins.dict[str, Any]]] = None
    color1: Optional[str] = None


@dataclass
class BlockAddResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    block_id: Optional[int] = None
    block: Optional[str] = None


@dataclass
class BlockUpdateCompanyDataRequest:
    name: str
    country: str
    postcode: str
    city: str
    street: str
    street_number: str
    door: str
    tax_number: str
    eu_tax_number: str


@dataclass
class BlockUpdateCompanyDataResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None


@dataclass
class BlockModifyRequest:
    block_name: str
    bank_number: str
    invoice_number_pre: str
    invoice_number_length: int
    invoice_issue: int
    email: str
    restart_number_by_year: int
    lang: str
    invoice_template: str
    currency: str
    other: builtins.list[builtins.dict[str, Any]]
    countryMustVisibleInInvoice: int
    bank_name: Optional[str] = None
    comment: Optional[str] = None
    logo: Optional[int] = None
    invoice_number_format: Optional[str] = None
    invoice_start: Optional[int] = None
    invoice_mails: Optional[int] = None
    invoice_mails_accounting: Optional[int] = None
    invoice_pdf_mail: Optional[int] = None
    invoice_pay_notice_mails: Optional[int] = None
    pdfProformGeneratePdf: Optional[int] = None
    pdfProformGeneratePdfSend: Optional[int] = None
    invoiceAppearance_paper: Optional[int] = None
    invoiceAppearance_edi: Optional[int] = None
    prepayment_invoice_enabled: Optional[int] = None
    reversevat_invoice_enabled: Optional[int] = None
    cashaccounting_invoice_enabled: Optional[int] = None
    smallBusinessIndicator: Optional[int] = None
    pdfHideCurrencyRate: Optional[int] = None
    bankPairingAutomaticInvoice: Optional[int] = None
    invoiceTax_EU_OSS: Optional[int] = None
    invoice_en16931_xml_attached: Optional[int] = None
    invoiceDigitalSignature: Optional[int] = None
    certificate_logo_visible: Optional[int] = None
    order_number_visible: Optional[int] = None
    pdfConvertZpl: Optional[int] = None
    pdfConvertZplDownload: Optional[int] = None
    pdf_design05: Optional[builtins.list[builtins.dict[str, Any]]] = None
    color1: Optional[str] = None


@dataclass
class BlockModifyResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    block_id: Optional[int] = None
    block: Optional[str] = None


@dataclass
class BlockListRequest:
    active: int


@dataclass
class BlockListResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    list: Optional[builtins.list[builtins.dict[str, Any]]] = None
    id: Optional[int] = None
    block_name: Optional[str] = None
    name: Optional[str] = None
    lang: Optional[str] = None
    currency: Optional[str] = None
    invoice_number_pre: Optional[str] = None
    active: Optional[int] = None


@dataclass
class BlockCloseRequest:
    block_id: int
    block_name: str


@dataclass
class BlockCloseResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None


@dataclass
class BlockOpenRequest:
    block_id: int
    block_name: str


@dataclass
class BlockOpenResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None


@dataclass
class CostCentreAddRequest:
    name: str
    code: str
    comment: Optional[str] = None
    orderby: Optional[int] = None
    is_default: Optional[int] = None


@dataclass
class CostCentreAddResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    code: Optional[str] = None


@dataclass
class CostCentreModifyRequest:
    name: str
    code: str
    comment: Optional[str] = None
    orderby: Optional[int] = None
    is_default: Optional[int] = None


@dataclass
class CostCentreModifyResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    code: Optional[str] = None


@dataclass
class CostCentreListRequest:
    pass


@dataclass
class CostCentreListResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    cost_centres: Optional[builtins.list[builtins.dict[str, Any]]] = None
    name: Optional[str] = None
    code: Optional[str] = None
    comment: Optional[int] = None


@dataclass
class CostCentreActivateRequest:
    code: str


@dataclass
class CostCentreActivateResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    code: Optional[str] = None


@dataclass
class CostCentreInactivateRequest:
    code: str


@dataclass
class CostCentreInactivateResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    code: Optional[str] = None


@dataclass
class CostTypeAddRequest:
    name: str
    code: str
    comment: Optional[str] = None
    orderby: Optional[int] = None
    is_default: Optional[int] = None


@dataclass
class CostTypeAddResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    code: Optional[str] = None


@dataclass
class CostTypeModifyRequest:
    name: str
    code: str
    comment: Optional[str] = None
    orderby: Optional[int] = None
    is_default: Optional[int] = None


@dataclass
class CostTypeModifyResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    code: Optional[str] = None


@dataclass
class CostTypeListRequest:
    pass


@dataclass
class CostTypeListResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    list: Optional[builtins.list[builtins.dict[str, Any]]] = None
    id: Optional[int] = None
    name: Optional[str] = None
    code: Optional[str] = None
    comment: Optional[str] = None
    orderby: Optional[int] = None
    is_default: Optional[int] = None
    active: Optional[int] = None


@dataclass
class CostTypeActivateRequest:
    code: str


@dataclass
class CostTypeActivateResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    code: Optional[str] = None


@dataclass
class CostTypeInactivateRequest:
    code: str


@dataclass
class CostTypeInactivateResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    code: Optional[str] = None


@dataclass
class ProjectListRequest:
    active: Optional[int] = None


@dataclass
class ProjectListResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    projects: Optional[builtins.list[builtins.dict[str, Any]]] = None


@dataclass
class ProjectGetRequest:
    code: str


@dataclass
class ProjectGetResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    id: Optional[int] = None
    code: Optional[str] = None
    name: Optional[str] = None
    is_booking: Optional[int] = None


@dataclass
class ProjectCreateRequest:
    code: str
    name: str
    customer_id: int
    block_id: int
    product_id: int
    quantities_id: int
    regularity: int
    net_price_single: Optional[str] = None
    minimum_minute: Optional[int] = None
    maximum_hour: Optional[int] = None
    maximum_task: Optional[int] = None
    admin_comment: Optional[str] = None
    pre_paid: Optional[int] = None
    is_repetitive: Optional[int] = None
    is_booking: Optional[int] = None
    active: Optional[int] = None


@dataclass
class ProjectCreateResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    id: Optional[int] = None
    code: Optional[str] = None


@dataclass
class ProjectInactivateRequest:
    code: str


@dataclass
class ProjectInactivateResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    code: Optional[str] = None


@dataclass
class ProjectTimesheetListRequest:
    code: str


@dataclass
class ProjectTimesheetListResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    timesheets: Optional[builtins.list[builtins.dict[str, Any]]] = None


@dataclass
class ProjectTimesheetStartRequest:
    code: str
    projects_workers_id: int
    comment: Optional[str] = None


@dataclass
class ProjectTimesheetStartResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    timesheet_id: Optional[int] = None


@dataclass
class ProjectTimesheetStopRequest:
    timesheet_id: int
    comment: Optional[str] = None


@dataclass
class ProjectTimesheetStopResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    timesheet_id: Optional[int] = None


@dataclass
class ProjectBookingSlotCreateRequest:
    code: str
    projects_workers_id: int
    start_date: str
    stop_date: str
    comment: Optional[str] = None


@dataclass
class ProjectBookingSlotCreateResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    slot_id: Optional[int] = None


@dataclass
class ProjectBookingBookRequest:
    timesheet_id: int
    customer_id: int


@dataclass
class ProjectBookingBookResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    timesheet_id: Optional[int] = None


@dataclass
class ProjectBookingCancelRequest:
    timesheet_id: int


@dataclass
class ProjectBookingCancelResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    timesheet_id: Optional[int] = None


@dataclass
class ProjectBookingCloseRequest:
    timesheet_id: int


@dataclass
class ProjectBookingCloseResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    timesheet_id: Optional[int] = None


@dataclass
class ProjectBookingBookDateRangeRequest:
    code: str
    customer_id: int
    date_from: str
    date_to: str


@dataclass
class ProjectBookingBookDateRangeResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    booking_group_id: Optional[str] = None
    nights: Optional[int] = None


@dataclass
class ProjectBookingCancelGroupRequest:
    booking_group_id: str


@dataclass
class ProjectBookingCancelGroupResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    booking_group_id: Optional[str] = None


@dataclass
class ProjectBookingCloseGroupRequest:
    booking_group_id: str
    comment: Optional[str] = None


@dataclass
class ProjectBookingCloseGroupResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    booking_group_id: Optional[str] = None


@dataclass
class ProjectBookingSetSlotPriceRequest:
    timesheet_id: int
    net_price_override: Optional[str] = None


@dataclass
class ProjectBookingSetSlotPriceResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    timesheet_id: Optional[int] = None


@dataclass
class ProjectAvailableSlotsRequest:
    code: str
    date_from: str
    date_to: str


@dataclass
class ProjectAvailableSlotsResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    slots: Optional[builtins.list[builtins.dict[str, Any]]] = None


@dataclass
class ProjectWorkerListRequest:
    pass


@dataclass
class ProjectWorkerListResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    workers: Optional[builtins.list[builtins.dict[str, Any]]] = None


@dataclass
class ProjectCalendarRequest:
    code: str
    year: int
    month: int


@dataclass
class ProjectCalendarResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    calendar: Optional[str] = None


@dataclass
class ProjectPassCreateRequest:
    code: str
    customer_id: int
    total_occasions: int
    product_id: Optional[int] = None
    net_price_single: Optional[str] = None
    auto_invoice: Optional[int] = None
    expiry_date: Optional[str] = None


@dataclass
class ProjectPassCreateResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    pass_id: Optional[int] = None


@dataclass
class ProjectPassListRequest:
    code: str


@dataclass
class ProjectPassListResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    passes: Optional[builtins.list[builtins.dict[str, Any]]] = None


@dataclass
class ProjectPassDeactivateRequest:
    pass_id: int


@dataclass
class ProjectPassDeactivateResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None


@dataclass
class ProjectPassUpdateExpiryRequest:
    pass_id: int
    expiry_date: str


@dataclass
class ProjectPassUpdateExpiryResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None


@dataclass
class TaxListRequest:
    type: str


@dataclass
class TaxListResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    list: Optional[builtins.list[builtins.dict[str, Any]]] = None
    id: Optional[int] = None
    name: Optional[str] = None
    code: Optional[str] = None
    value: Optional[float] = None
    active: Optional[int] = None
    is_default: Optional[int] = None
    vatType: Optional[str] = None
    vatSubType: Optional[str] = None
    taxTypeDesc: Optional[str] = None


@dataclass
class TaxAddRequest:
    name: str
    code: str
    value: float
    is_default: Optional[int] = None
    other: Optional[str] = None


@dataclass
class TaxAddResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    code: Optional[str] = None


@dataclass
class TaxModifyRequest:
    name: str
    code: str
    value: float
    is_default: Optional[int] = None
    other: Optional[str] = None


@dataclass
class TaxModifyResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    code: Optional[str] = None


@dataclass
class TaxActivateRequest:
    code: str


@dataclass
class TaxActivateResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    code: Optional[str] = None


@dataclass
class TaxInactivateRequest:
    code: str


@dataclass
class TaxInactivateResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    code: Optional[str] = None


@dataclass
class PaymentModeInactivateRequest:
    code: str


@dataclass
class PaymentModeInactivateResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None


@dataclass
class PaymentModeActivateRequest:
    code: str


@dataclass
class PaymentModeActivateResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None


@dataclass
class PaymentModeDownloadRequest:
    pass


@dataclass
class PaymentModeDownloadResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    list: Optional[builtins.list[builtins.dict[str, Any]]] = None
    id: Optional[int] = None
    name: Optional[str] = None
    code: Optional[str] = None
    active: Optional[int] = None
    is_default: Optional[int] = None


@dataclass
class OrderAddRequest:
    proform_order: int
    customer_sid: str
    payment_mode_id: int
    trade_date: str
    print_date: str
    pay_date: str
    elements: builtins.list[builtins.dict[str, Any]]
    product_sid: str
    amount: float
    quantity: str
    tax_code: str
    order_date: str
    paid: int
    currency: str
    lang: Optional[str] = None
    order_number: Optional[str] = None
    comment: Optional[str] = None
    net_price_single: Optional[float] = None
    gross_price_single: Optional[float] = None
    other: Optional[str] = None
    discount_type: Optional[str] = None
    discount_value: Optional[float] = None
    regularities_id: Optional[int] = None
    regularity: Optional[str] = None
    regularities_date: Optional[str] = None
    meta: Optional[builtins.list[builtins.dict[str, Any]]] = None
    KULCS: Optional[str] = None


@dataclass
class OrderAddResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    order_id: Optional[int] = None
    order_number: Optional[str] = None
    invoice_number: Optional[str] = None
    invoice_client_url: Optional[str] = None


@dataclass
class OrderCollectiveAddRequest:
    customer_sid: str
    payment_mode_id: int
    trade_date: str
    print_date: str
    pay_date: str
    elements: builtins.list[builtins.dict[str, Any]]
    product_sid: str
    amount: float
    quantity: str
    tax_code: str
    order_date: str
    paid: int
    currency: str
    lang: Optional[str] = None
    order_number: Optional[str] = None
    comment: Optional[str] = None
    net_price_single: Optional[float] = None
    gross_price_single: Optional[float] = None
    regularity: Optional[str] = None
    regularities_date: Optional[str] = None


@dataclass
class OrderCollectiveAddResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    order_id: Optional[int] = None
    order_number: Optional[str] = None


@dataclass
class OrderListRequest:
    limit: Optional[int] = None
    page: Optional[int] = None
    from_: Optional[str] = None
    to: Optional[str] = None
    customer_sid: Optional[str] = None
    regularities_id: Optional[int] = None
    regularity: Optional[str] = None
    type: Optional[str] = None


@dataclass
class OrderListResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    numberOfResults: Optional[int] = None
    numberOfPages: Optional[int] = None
    orders: Optional[builtins.list[builtins.dict[str, Any]]] = None
    order_number: Optional[str] = None
    block_id: Optional[int] = None
    print_date: Optional[str] = None
    trade_date: Optional[str] = None
    pay_date: Optional[str] = None
    order_date: Optional[str] = None
    regularities_id: Optional[int] = None
    regularity: Optional[str] = None
    regularities_date: Optional[str] = None
    invoice_to_post: Optional[int] = None
    invoice_to_post_code: Optional[str] = None
    collective: Optional[int] = None
    type: Optional[int] = None
    type_code: Optional[str] = None
    payment_mode_id: Optional[int] = None
    payment_mode_code: Optional[str] = None
    comment: Optional[str] = None
    admin_comment: Optional[str] = None
    net_price: Optional[float] = None
    tax_value: Optional[float] = None
    gross_price: Optional[float] = None
    currency_id: Optional[int] = None
    currency: Optional[str] = None
    customer_sid: Optional[str] = None
    customer_legal_status: Optional[str] = None
    customer_name: Optional[str] = None
    customer_country: Optional[str] = None
    customer_city: Optional[str] = None
    customer_postcode: Optional[str] = None
    customer_street: Optional[str] = None
    customer_email: Optional[str] = None
    customer_tax_number: Optional[str] = None
    customer_eu_tax_number: Optional[str] = None
    customer_lang: Optional[str] = None
    paid: Optional[int] = None
    paid_code: Optional[str] = None


@dataclass
class OrderStornoRequest:
    order_number: str
    admin_comment: Optional[str] = None
    storno_reason: Optional[str] = None
    refund: Optional[int] = None
    comment: Optional[str] = None


@dataclass
class OrderStornoResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    order_number: Optional[str] = None
    invoice_number: Optional[str] = None


@dataclass
class OrderProformDownloadRequest:
    order_number: str


@dataclass
class OrderProformDownloadResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    proform_id: Optional[int] = None
    proform_number: Optional[str] = None
    proform_file_size: Optional[int] = None
    proform: Optional[str] = None


@dataclass
class OrderBillRequest:
    order_number: str
    paid: int
    payment_mode_id: Optional[int] = None


@dataclass
class OrderBillResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    invoice_number: Optional[str] = None
    invoice_client_url: Optional[str] = None
    invoices: Optional[builtins.list[builtins.dict[str, Any]]] = None
    invoice_id: Optional[int] = None
    invoice_type_id: Optional[int] = None
    invoice_type: Optional[str] = None
    invoice_file_size: Optional[int] = None
    invoice: Optional[str] = None


@dataclass
class OrderDetailsRequest:
    order_number: str


@dataclass
class OrderDetailsResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    customer_sid: Optional[str] = None
    name: Optional[str] = None
    country: Optional[str] = None
    postcode: Optional[str] = None
    city: Optional[str] = None
    street: Optional[str] = None
    street_number: Optional[str] = None
    door: Optional[str] = None
    tax_number: Optional[str] = None
    eu_tax_number: Optional[str] = None
    currency: Optional[str] = None
    currency_id: Optional[int] = None
    order_number: Optional[str] = None
    payment_mode_id: Optional[int] = None
    payment_mode: Optional[str] = None
    trade_date: Optional[str] = None
    print_date: Optional[str] = None
    pay_date: Optional[str] = None
    comment: Optional[int] = None
    net_price: Optional[str] = None
    tax_value: Optional[str] = None
    gross_price: Optional[str] = None
    elements: Optional[builtins.list[builtins.dict[str, Any]]] = None
    product_sid: Optional[str] = None
    amount: Optional[float] = None
    quantity: Optional[str] = None
    net_price_single: Optional[float] = None
    tax: Optional[float] = None
    other: Optional[str] = None
    other_json: Optional[str] = None
    order_date: Optional[str] = None
    invoice_to_post: Optional[int] = None
    invoice_to_post_code: Optional[str] = None
    collective: Optional[int] = None
    regularities_id: Optional[int] = None
    regularities_date: Optional[str] = None
    invoices: Optional[str] = None
    admin_comment: Optional[str] = None
    api_invoice: Optional[int] = None


@dataclass
class OrderCollectiveCloseRequest:
    customer_sid: str


@dataclass
class OrderCollectiveCloseResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    invoice_number: Optional[str] = None


@dataclass
class OrderCollectiveSettlingRequest:
    order_number: str
    invoice_number: str


@dataclass
class OrderCollectiveSettlingResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    list: Optional[builtins.list[builtins.dict[str, Any]]] = None
    order_number: Optional[str] = None
    invoice_number: Optional[str] = None
    customer_sid: Optional[str] = None
    services_sid: Optional[str] = None
    service: Optional[str] = None
    amount: Optional[float] = None
    net_price: Optional[float] = None
    tax_value: Optional[float] = None
    gross_price: Optional[float] = None
    currency: Optional[str] = None
    confirmed: Optional[int] = None
    other: Optional[str] = None


@dataclass
class OrderCollectiveAddElementsRequest:
    customer_sid: str
    elements: builtins.list[builtins.dict[str, Any]]
    product_sid: str
    amount: float
    quantity: str
    net_price_single: float
    tax_code: str
    comment: Optional[str] = None
    other: Optional[str] = None


@dataclass
class OrderCollectiveAddElementsResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    order_id: Optional[int] = None
    order_number: Optional[str] = None


@dataclass
class OrderSetPaidRequest:
    order_number: str


@dataclass
class OrderSetPaidResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    paid: Optional[int] = None
    paid_code: Optional[str] = None


@dataclass
class OrderCheckPaidRequest:
    order_number: str


@dataclass
class OrderCheckPaidResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    paid: Optional[int] = None
    paid_code: Optional[str] = None


@dataclass
class OrderPaidChangeListRequest:
    pass


@dataclass
class OrderPaidChangeListResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    list: Optional[builtins.list[builtins.dict[str, Any]]] = None
    order_number: Optional[str] = None


@dataclass
class InvoiceAddRequest:
    customer_sid: str
    payment_mode_id: int
    trade_date: str
    print_date: str
    pay_date: str
    elements: builtins.list[builtins.dict[str, Any]]
    product_sid: str
    amount: float
    quantity: str
    tax_code: str
    order_date: str
    paid: int
    currency: str
    prepayment: int
    lang: Optional[str] = None
    order_number: Optional[str] = None
    comment: Optional[str] = None
    net_price_single: Optional[float] = None
    gross_price_single: Optional[float] = None
    other: Optional[str] = None
    discount_type: Optional[str] = None
    discount_value: Optional[float] = None


@dataclass
class InvoiceAddResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    invoice_number: Optional[str] = None
    invoice_client_url: Optional[str] = None


@dataclass
class InvoiceAddPrepaymentRequest:
    customer_sid: str
    payment_mode_id: int
    trade_date: str
    print_date: str
    pay_date: str
    elements: builtins.list[builtins.dict[str, Any]]
    product_sid: str
    amount: float
    quantity: str
    net_price_single: float
    tax_code: str
    order_date: str
    paid: int
    currency: str
    lang: Optional[str] = None
    order_number: Optional[str] = None
    comment: Optional[str] = None
    other: Optional[str] = None
    discount_type: Optional[str] = None
    discount_value: Optional[float] = None


@dataclass
class InvoiceAddPrepaymentResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    invoice_number: Optional[str] = None
    invoice_client_url: Optional[str] = None


@dataclass
class InvoiceAddFinalRequest:
    customer_sid: str
    payment_mode_id: int
    trade_date: str
    print_date: str
    pay_date: str
    elements: builtins.list[builtins.dict[str, Any]]
    product_sid: str
    amount: float
    quantity: str
    net_price_single: float
    tax_code: str
    order_date: str
    paid: int
    currency: str
    lang: Optional[str] = None
    order_number: Optional[str] = None
    comment: Optional[str] = None
    other: Optional[str] = None
    discount_type: Optional[str] = None
    discount_value: Optional[float] = None


@dataclass
class InvoiceAddFinalResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    invoice_number: Optional[str] = None
    invoice_client_url: Optional[str] = None


@dataclass
class InvoiceDetailsRequest:
    invoice_number: str


@dataclass
class InvoiceDetailsResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    invoice_number: Optional[str] = None
    customer_sid: Optional[str] = None
    name: Optional[str] = None
    country: Optional[str] = None
    postcode: Optional[str] = None
    city: Optional[str] = None
    street: Optional[str] = None
    street_number: Optional[str] = None
    door: Optional[str] = None
    tax_number: Optional[str] = None
    eu_tax_number: Optional[str] = None
    currency: Optional[str] = None
    currency_id: Optional[int] = None
    order_number: Optional[str] = None
    payment_mode_id: Optional[int] = None
    payment_mode: Optional[str] = None
    trade_date: Optional[str] = None
    print_date: Optional[str] = None
    pay_date: Optional[str] = None
    comment: Optional[int] = None
    net_price: Optional[str] = None
    tax_value: Optional[str] = None
    gross_price: Optional[str] = None
    elements: Optional[builtins.list[builtins.dict[str, Any]]] = None
    product_sid: Optional[str] = None
    amount: Optional[float] = None
    quantity: Optional[str] = None
    net_price_single: Optional[float] = None
    tax: Optional[float] = None
    tax_code: Optional[str] = None
    other: Optional[str] = None
    other_json: Optional[str] = None
    order_date: Optional[str] = None
    block_name: Optional[str] = None
    invoice_to_post: Optional[int] = None
    invoice_to_post_code: Optional[str] = None
    api_invoice: Optional[int] = None


@dataclass
class InvoiceDownloadRequest:
    invoice_number: str
    invoice_type: str


@dataclass
class InvoiceDownloadResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    invoices: Optional[builtins.list[builtins.dict[str, Any]]] = None
    invoice_id: Optional[int] = None
    invoice_number: Optional[str] = None
    invoice_type_id: Optional[int] = None
    invoice_type: Optional[str] = None
    invoice_file_size: Optional[int] = None
    invoice: Optional[str] = None


@dataclass
class InvoiceStornoRequest:
    invoice_number: str
    admin_comment: Optional[str] = None
    storno_reason: Optional[str] = None
    refund: Optional[int] = None
    comment: Optional[str] = None


@dataclass
class InvoiceStornoResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    invoice_number: Optional[str] = None


@dataclass
class InvoiceListRequest:
    limit: Optional[int] = None
    page: Optional[int] = None
    from_: Optional[str] = None
    to: Optional[str] = None
    customer_sid: Optional[str] = None


@dataclass
class InvoiceListResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    numberOfResults: Optional[int] = None
    numberOfPages: Optional[int] = None
    invoices: Optional[builtins.list[builtins.dict[str, Any]]] = None
    invoice_id: Optional[int] = None
    invoice_number: Optional[str] = None
    customer_sid: Optional[str] = None
    customer_legal_status: Optional[str] = None
    customer_name: Optional[str] = None
    customer_country: Optional[str] = None
    customer_postcode: Optional[str] = None
    customer_city: Optional[str] = None
    customer_street: Optional[str] = None
    customer_street_number: Optional[str] = None
    customer_door: Optional[str] = None
    customer_tax_number: Optional[str] = None
    customer_eu_tax_number: Optional[str] = None
    customer_region: Optional[str] = None
    customer_phone: Optional[str] = None
    customer_email: Optional[str] = None
    customer_lang: Optional[str] = None
    trade_date: Optional[str] = None
    print_date: Optional[str] = None
    pay_date: Optional[str] = None
    type: Optional[int] = None
    type_code: Optional[str] = None
    reference: Optional[str] = None
    payment_mode_id: Optional[int] = None
    comment: Optional[int] = None
    net_price: Optional[float] = None
    tax_value: Optional[float] = None
    gross_price: Optional[float] = None
    currency: Optional[str] = None
    currency_id: Optional[int] = None
    paid: Optional[int] = None
    paid_code: Optional[str] = None
    invoice_type_id: Optional[int] = None
    invoice_type: Optional[str] = None
    invoice_file_size: Optional[int] = None
    invoice: Optional[str] = None


@dataclass
class InvoiceExportRequest:
    date_from: Optional[str] = None
    date_to: Optional[str] = None
    number_from: Optional[str] = None
    number_to: Optional[str] = None


@dataclass
class InvoiceExportResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    invoice_export_file: Optional[str] = None


@dataclass
class InvoiceSearchRequest:
    search_type_code: str
    search: str


@dataclass
class InvoiceSearchResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    invoice_number: Optional[str] = None
    customer_sid: Optional[str] = None
    name: Optional[str] = None
    country: Optional[str] = None
    postcode: Optional[str] = None
    city: Optional[str] = None
    street: Optional[str] = None
    street_number: Optional[str] = None
    door: Optional[str] = None
    tax_number: Optional[str] = None
    eu_tax_number: Optional[str] = None
    currency_id: Optional[int] = None
    currency: Optional[str] = None
    order_number: Optional[str] = None
    payment_mode_id: Optional[int] = None
    payment_mode_code: Optional[str] = None
    trade_date: Optional[str] = None
    print_date: Optional[str] = None
    pay_date: Optional[str] = None
    comment: Optional[str] = None
    net_price: Optional[float] = None
    tax_value: Optional[float] = None
    gross_price: Optional[float] = None
    elements: Optional[builtins.list[builtins.dict[str, Any]]] = None
    product_sid: Optional[str] = None
    product_name: Optional[str] = None
    product_service_id: Optional[str] = None
    amount: Optional[float] = None
    quantity: Optional[str] = None
    net_price_single: Optional[float] = None
    tax: Optional[float] = None
    other: Optional[str] = None
    other_json: Optional[str] = None
    order_date: Optional[str] = None
    invoice_type: Optional[str] = None


@dataclass
class InvoiceCorrectionRequest:
    invoice_number: str
    elementsStorno: builtins.list[builtins.dict[str, Any]]
    elements: builtins.list[builtins.dict[str, Any]]
    quantity: str
    net_price_single: float
    tax_code: str
    payment_mode_id: int
    product_sid: Optional[int] = None
    amount: Optional[int] = None
    comment: Optional[str] = None
    other: Optional[str] = None
    trade_date: Optional[str] = None
    pay_date: Optional[str] = None
    paid: Optional[int] = None


@dataclass
class InvoiceCorrectionResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    invoice_number: Optional[str] = None


@dataclass
class InvoiceResendRequest:
    invoice_number: str


@dataclass
class InvoiceResendResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    invoice_number: Optional[str] = None
    invoice_to_post: Optional[int] = None
    invoice_to_post_code: Optional[str] = None


@dataclass
class InvoiceCheckPaidRequest:
    invoice_number: str


@dataclass
class InvoiceCheckPaidResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    paid: Optional[int] = None
    paid_code: Optional[str] = None


@dataclass
class InvoiceSetPaidRequest:
    invoice_number: str


@dataclass
class InvoiceSetPaidResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    paid: Optional[int] = None
    paid_code: Optional[str] = None


@dataclass
class DebtDetailsRequest:
    type: str
    customer_sid: str
    invoice_number: str


@dataclass
class DebtDetailsResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    debt: Optional[Any] = None


@dataclass
class DebtDownloadRequest:
    invoice_number: str
    invoice_type: str


@dataclass
class DebtDownloadResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    file: Optional[str] = None
    file_size: Optional[int] = None


@dataclass
class DebtListRequest:
    type: Optional[int] = None
    active: Optional[int] = None
    paid: Optional[int] = None
    customer_sid: Optional[str] = None
    limit: Optional[int] = None
    page: Optional[int] = None
    from_: Optional[str] = None
    to: Optional[str] = None


@dataclass
class DebtListResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    numberOfResults: Optional[int] = None
    numberOfPages: Optional[int] = None
    list: Optional[builtins.list[builtins.dict[str, Any]]] = None


@dataclass
class DebtAddRequest:
    customer_sid: str
    invoice_number: str
    amount: float
    currency: str
    trade_date: str
    print_date: str
    pay_date: str
    currency_id: Optional[int] = None
    payment_date: Optional[str] = None
    payment_mode: Optional[str] = None
    payment_mode_id: Optional[int] = None
    paid: Optional[int] = None
    paid_code: Optional[str] = None
    cost_centre: Optional[str] = None
    cost_type: Optional[str] = None
    invoice_reference: Optional[str] = None
    bank_comment: Optional[str] = None
    comment: Optional[str] = None
    invoice_file: Optional[str] = None


@dataclass
class DebtAddResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    debt_id: Optional[int] = None


@dataclass
class DebtModifyRequest:
    id: int
    customer_sid: Optional[str] = None
    invoice_number: Optional[str] = None
    amount: Optional[float] = None
    currency: Optional[str] = None
    currency_id: Optional[int] = None
    trade_date: Optional[str] = None
    print_date: Optional[str] = None
    pay_date: Optional[str] = None
    payment_date: Optional[str] = None
    payment_mode: Optional[str] = None
    payment_mode_id: Optional[int] = None
    paid: Optional[int] = None
    paid_code: Optional[str] = None
    cost_centre: Optional[str] = None
    cost_type: Optional[str] = None
    invoice_reference: Optional[str] = None
    bank_comment: Optional[str] = None
    comment: Optional[str] = None
    invoice_file: Optional[str] = None


@dataclass
class DebtModifyResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    debt_id: Optional[int] = None


@dataclass
class DebtAcceptRequest:
    debt_ids: builtins.list[builtins.dict[str, Any]]


@dataclass
class DebtAcceptResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    accepted_count: Optional[int] = None


@dataclass
class DebtPayRequest:
    debt_ids: builtins.list[builtins.dict[str, Any]]


@dataclass
class DebtPayResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    paid_count: Optional[int] = None


@dataclass
class DebtDeleteRequest:
    debt_ids: builtins.list[builtins.dict[str, Any]]


@dataclass
class DebtDeleteResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    deleted_count: Optional[int] = None


@dataclass
class DebtGenerateRequest:
    debt_ids: builtins.list[builtins.dict[str, Any]]


@dataclass
class DebtGenerateResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    file: Optional[str] = None
    file_size: Optional[int] = None


@dataclass
class DebtExportRequest:
    dateFrom: str
    dateTo: str


@dataclass
class DebtExportResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    list: Optional[builtins.list[builtins.dict[str, Any]]] = None


@dataclass
class SystemMessageListRequest:
    pass


@dataclass
class SystemMessageListResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    list: Optional[builtins.list[builtins.dict[str, Any]]] = None
    id: Optional[int] = None
    message: Optional[str] = None
    message_date: Optional[str] = None
    message_type: Optional[int] = None


@dataclass
class SystemMessageSetReadRequest:
    id: int


@dataclass
class SystemMessageSetReadResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None


@dataclass
class SystemErrorCodeListRequest:
    lang: Optional[str] = None


@dataclass
class SystemErrorCodeListResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    lang: Optional[builtins.list[builtins.dict[str, Any]]] = None
    code: Optional[int] = None
    description: Optional[str] = None
    type: Optional[str] = None


@dataclass
class GetVersionRequest:
    pass


@dataclass
class GetVersionResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    version: Optional[str] = None


@dataclass
class ServiceProviderDatasRequest:
    pass


@dataclass
class ServiceProviderDatasResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    hosting_name: Optional[str] = None
    hosting_address: Optional[str] = None
    hosting_tax_number: Optional[str] = None
    hosting_email: Optional[str] = None
    hosting_phone: Optional[str] = None
    hosting_customer_service_langs: Optional[str] = None
    hosting_customer_service_times: Optional[str] = None
    hosting_bank_name: Optional[str] = None
    hosting_bank_number: Optional[str] = None
    hosting_service_url: Optional[str] = None
    hosting_service_start_date: Optional[str] = None
    hosting_service_version: Optional[str] = None
    instance_web_url: Optional[str] = None
    instance_soap_url: Optional[str] = None
    instance_rest_url: Optional[str] = None


@dataclass
class CompanyDataRequest:
    pass


@dataclass
class CompanyDataResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    id: Optional[int] = None
    block_name: Optional[str] = None
    name: Optional[str] = None
    country: Optional[str] = None
    postcode: Optional[str] = None
    city: Optional[str] = None
    street: Optional[str] = None
    street_number: Optional[str] = None
    door: Optional[str] = None
    tax_number: Optional[str] = None
    eu_tax_number: Optional[str] = None
    bank_number: Optional[str] = None
    invoice_number_pre: Optional[str] = None
    invoice_number_length: Optional[int] = None
    email: Optional[str] = None
    comment: Optional[str] = None
    invoice_footer: Optional[str] = None
    invoice_issue: Optional[int] = None
    restart_number_by_year: Optional[int] = None
    lang: Optional[str] = None
    date: Optional[str] = None
    invoice_template: Optional[str] = None
    admin_users_id: Optional[int] = None
    currency_id: Optional[int] = None
    active: Optional[int] = None
    bank_name: Optional[str] = None
    currency: Optional[str] = None


@dataclass
class QuantityListRequest:
    type: str


@dataclass
class QuantityListResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    list: Optional[builtins.list[builtins.dict[str, Any]]] = None
    id: Optional[int] = None
    name: Optional[str] = None
    code: Optional[str] = None
    active: Optional[int] = None
    is_default: Optional[int] = None
    unitOfMeasure: Optional[str] = None


@dataclass
class CurrencyDownloadRequest:
    type: str


@dataclass
class CurrencyDownloadResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    list: Optional[builtins.list[builtins.dict[str, Any]]] = None
    id: Optional[int] = None
    currency: Optional[str] = None
    amount: Optional[float] = None
    unit: Optional[float] = None
    date: Optional[str] = None


@dataclass
class RegularityDownloadRequest:
    pass


@dataclass
class RegularityDownloadResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    list: Optional[builtins.list[builtins.dict[str, Any]]] = None
    id: Optional[int] = None
    code: Optional[str] = None
    regularity: Optional[str] = None


@dataclass
class CountryDownloadRequest:
    pass


@dataclass
class CountryDownloadResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    list: Optional[builtins.list[builtins.dict[str, Any]]] = None
    code: Optional[str] = None
    country: Optional[str] = None


@dataclass
class PostcodeDownloadRequest:
    country: str


@dataclass
class PostcodeDownloadResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    postcodes: Optional[builtins.list[builtins.dict[str, Any]]] = None
    postcode: Optional[str] = None
    city: Optional[str] = None
    region: Optional[str] = None


@dataclass
class PingRequest:
    pass


@dataclass
class PingResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None


@dataclass
class MonitorRequest:
    pass


@dataclass
class MonitorResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    list: Optional[builtins.list[builtins.dict[str, Any]]] = None
    state: Optional[str] = None
    name: Optional[str] = None
    last_check: Optional[str] = None


class SzamlaiktatoAPI:
    def __init__(self, client: OnlineSzamlazoClient):
        self.client = client

    def _invoke(
        self,
        method: str,
        request: Any,
        response_cls: Any,
        skip_block: bool = False,
        requires_instance_id: bool = False,
        req_mapping: Optional[builtins.dict[str, str]] = None,
        resp_mapping: Optional[builtins.dict[str, str]] = None,
    ) -> Any:
        params = asdict(request) if request else {}
        if req_mapping:
            for py_name, orig_name in req_mapping.items():
                if py_name in params:
                    params[orig_name] = params.pop(py_name)
        data = self.client._call(
            method,
            params,
            skip_block=skip_block,
            requires_instance_id=requires_instance_id,
        )
        if resp_mapping:
            for orig_name, py_name in resp_mapping.items():
                if orig_name in data:
                    data[py_name] = data.pop(orig_name)
        valid_keys = response_cls.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return response_cls(**filtered_data)

    def install(self, request: InstallRequest) -> InstallResponse:
        return self._invoke(
            "install",
            request,
            InstallResponse,
            skip_block=True,
        )

    def update(self, request: UpdateRequest) -> UpdateResponse:
        return self._invoke(
            "update",
            request,
            UpdateResponse,
            skip_block=True,
        )

    def customerAdd(self, request: CustomerAddRequest) -> CustomerAddResponse:
        return self._invoke(
            "customerAdd",
            request,
            CustomerAddResponse,
            requires_instance_id=True,
        )

    def customerModify(self, request: CustomerModifyRequest) -> CustomerModifyResponse:
        return self._invoke(
            "customerModify",
            request,
            CustomerModifyResponse,
            requires_instance_id=True,
        )

    def customerGet(self, request: CustomerGetRequest) -> CustomerGetResponse:
        return self._invoke(
            "customerGet",
            request,
            CustomerGetResponse,
            requires_instance_id=True,
        )

    def customerActivate(
        self, request: CustomerActivateRequest
    ) -> CustomerActivateResponse:
        return self._invoke(
            "customerActivate",
            request,
            CustomerActivateResponse,
            requires_instance_id=True,
        )

    def customerInactivate(
        self, request: CustomerInactivateRequest
    ) -> CustomerInactivateResponse:
        return self._invoke(
            "customerInactivate",
            request,
            CustomerInactivateResponse,
            requires_instance_id=True,
        )

    def customerSwap(self, request: CustomerSwapRequest) -> CustomerSwapResponse:
        return self._invoke(
            "customerSwap",
            request,
            CustomerSwapResponse,
            requires_instance_id=True,
        )

    def customerList(self, request: CustomerListRequest) -> CustomerListResponse:
        return self._invoke(
            "customerList",
            request,
            CustomerListResponse,
            skip_block=True,
            requires_instance_id=True,
        )

    def productAdd(self, request: ProductAddRequest) -> ProductAddResponse:
        return self._invoke(
            "productAdd",
            request,
            ProductAddResponse,
            requires_instance_id=True,
        )

    def productModify(self, request: ProductModifyRequest) -> ProductModifyResponse:
        return self._invoke(
            "productModify",
            request,
            ProductModifyResponse,
            requires_instance_id=True,
        )

    def productGet(self, request: ProductGetRequest) -> ProductGetResponse:
        return self._invoke(
            "productGet",
            request,
            ProductGetResponse,
            requires_instance_id=True,
        )

    def productActivate(
        self, request: ProductActivateRequest
    ) -> ProductActivateResponse:
        return self._invoke(
            "productActivate",
            request,
            ProductActivateResponse,
            requires_instance_id=True,
        )

    def productInactivate(
        self, request: ProductInactivateRequest
    ) -> ProductInactivateResponse:
        return self._invoke(
            "productInactivate",
            request,
            ProductInactivateResponse,
            requires_instance_id=True,
        )

    def productList(self, request: ProductListRequest) -> ProductListResponse:
        return self._invoke(
            "productList",
            request,
            ProductListResponse,
            skip_block=True,
            requires_instance_id=True,
        )

    def productFileList(
        self, request: ProductFileListRequest
    ) -> ProductFileListResponse:
        return self._invoke(
            "productFileList",
            request,
            ProductFileListResponse,
            skip_block=True,
            requires_instance_id=True,
        )

    def outerDatasources(
        self, request: Optional[OuterDatasourcesRequest] = None
    ) -> OuterDatasourcesResponse:
        return self._invoke(
            "outerDatasources",
            request,
            OuterDatasourcesResponse,
            skip_block=True,
            requires_instance_id=True,
        )

    def outerDatasourcesGet(
        self, request: OuterDatasourcesGetRequest
    ) -> OuterDatasourcesGetResponse:
        return self._invoke(
            "outerDatasourcesGet",
            request,
            OuterDatasourcesGetResponse,
            skip_block=True,
            requires_instance_id=True,
        )

    def outerDatasourcesSave(
        self, request: OuterDatasourcesSaveRequest
    ) -> OuterDatasourcesSaveResponse:
        return self._invoke(
            "outerDatasourcesSave",
            request,
            OuterDatasourcesSaveResponse,
            skip_block=True,
            requires_instance_id=True,
        )

    def adminUserAdd(self, request: AdminUserAddRequest) -> AdminUserAddResponse:
        return self._invoke(
            "adminUserAdd",
            request,
            AdminUserAddResponse,
            skip_block=True,
            requires_instance_id=True,
        )

    def adminUserPassword(
        self, request: AdminUserPasswordRequest
    ) -> AdminUserPasswordResponse:
        return self._invoke(
            "adminUserPassword",
            request,
            AdminUserPasswordResponse,
            skip_block=True,
            requires_instance_id=True,
        )

    def adminUserDel(self, request: AdminUserDelRequest) -> AdminUserDelResponse:
        return self._invoke(
            "adminUserDel",
            request,
            AdminUserDelResponse,
            skip_block=True,
            requires_instance_id=True,
        )

    def blockAdd(self, request: BlockAddRequest) -> BlockAddResponse:
        return self._invoke(
            "blockAdd",
            request,
            BlockAddResponse,
            skip_block=True,
            requires_instance_id=True,
        )

    def blockUpdateCompanyData(
        self, request: BlockUpdateCompanyDataRequest
    ) -> BlockUpdateCompanyDataResponse:
        return self._invoke(
            "blockUpdateCompanyData",
            request,
            BlockUpdateCompanyDataResponse,
            skip_block=True,
            requires_instance_id=True,
        )

    def blockModify(self, request: BlockModifyRequest) -> BlockModifyResponse:
        return self._invoke(
            "blockModify",
            request,
            BlockModifyResponse,
            skip_block=True,
            requires_instance_id=True,
        )

    def blockList(self, request: BlockListRequest) -> BlockListResponse:
        return self._invoke(
            "blockList",
            request,
            BlockListResponse,
            skip_block=True,
            requires_instance_id=True,
        )

    def blockClose(self, request: BlockCloseRequest) -> BlockCloseResponse:
        return self._invoke(
            "blockClose",
            request,
            BlockCloseResponse,
            skip_block=True,
            requires_instance_id=True,
        )

    def blockOpen(self, request: BlockOpenRequest) -> BlockOpenResponse:
        return self._invoke(
            "blockOpen",
            request,
            BlockOpenResponse,
            skip_block=True,
            requires_instance_id=True,
        )

    def costCentreAdd(self, request: CostCentreAddRequest) -> CostCentreAddResponse:
        return self._invoke(
            "costCentreAdd",
            request,
            CostCentreAddResponse,
            skip_block=True,
            requires_instance_id=True,
        )

    def costCentreModify(
        self, request: CostCentreModifyRequest
    ) -> CostCentreModifyResponse:
        return self._invoke(
            "costCentreModify",
            request,
            CostCentreModifyResponse,
            skip_block=True,
            requires_instance_id=True,
        )

    def costCentreList(
        self, request: Optional[CostCentreListRequest] = None
    ) -> CostCentreListResponse:
        return self._invoke(
            "costCentreList",
            request,
            CostCentreListResponse,
            skip_block=True,
            requires_instance_id=True,
        )

    def costCentreActivate(
        self, request: CostCentreActivateRequest
    ) -> CostCentreActivateResponse:
        return self._invoke(
            "costCentreActivate",
            request,
            CostCentreActivateResponse,
            skip_block=True,
            requires_instance_id=True,
        )

    def costCentreInactivate(
        self, request: CostCentreInactivateRequest
    ) -> CostCentreInactivateResponse:
        return self._invoke(
            "costCentreInactivate",
            request,
            CostCentreInactivateResponse,
            skip_block=True,
            requires_instance_id=True,
        )

    def costTypeAdd(self, request: CostTypeAddRequest) -> CostTypeAddResponse:
        return self._invoke(
            "costTypeAdd",
            request,
            CostTypeAddResponse,
            skip_block=True,
            requires_instance_id=True,
        )

    def costTypeModify(self, request: CostTypeModifyRequest) -> CostTypeModifyResponse:
        return self._invoke(
            "costTypeModify",
            request,
            CostTypeModifyResponse,
            skip_block=True,
            requires_instance_id=True,
        )

    def costTypeList(
        self, request: Optional[CostTypeListRequest] = None
    ) -> CostTypeListResponse:
        return self._invoke(
            "costTypeList",
            request,
            CostTypeListResponse,
            skip_block=True,
            requires_instance_id=True,
        )

    def costTypeActivate(
        self, request: CostTypeActivateRequest
    ) -> CostTypeActivateResponse:
        return self._invoke(
            "costTypeActivate",
            request,
            CostTypeActivateResponse,
            skip_block=True,
            requires_instance_id=True,
        )

    def costTypeInactivate(
        self, request: CostTypeInactivateRequest
    ) -> CostTypeInactivateResponse:
        return self._invoke(
            "costTypeInactivate",
            request,
            CostTypeInactivateResponse,
            skip_block=True,
            requires_instance_id=True,
        )

    def projectList(self, request: ProjectListRequest) -> ProjectListResponse:
        return self._invoke(
            "projectList",
            request,
            ProjectListResponse,
            skip_block=True,
            requires_instance_id=True,
        )

    def projectGet(self, request: ProjectGetRequest) -> ProjectGetResponse:
        return self._invoke(
            "projectGet",
            request,
            ProjectGetResponse,
            skip_block=True,
            requires_instance_id=True,
        )

    def projectCreate(self, request: ProjectCreateRequest) -> ProjectCreateResponse:
        return self._invoke(
            "projectCreate",
            request,
            ProjectCreateResponse,
            skip_block=True,
            requires_instance_id=True,
        )

    def projectInactivate(
        self, request: ProjectInactivateRequest
    ) -> ProjectInactivateResponse:
        return self._invoke(
            "projectInactivate",
            request,
            ProjectInactivateResponse,
            skip_block=True,
            requires_instance_id=True,
        )

    def projectTimesheetList(
        self, request: ProjectTimesheetListRequest
    ) -> ProjectTimesheetListResponse:
        return self._invoke(
            "projectTimesheetList",
            request,
            ProjectTimesheetListResponse,
            skip_block=True,
            requires_instance_id=True,
        )

    def projectTimesheetStart(
        self, request: ProjectTimesheetStartRequest
    ) -> ProjectTimesheetStartResponse:
        return self._invoke(
            "projectTimesheetStart",
            request,
            ProjectTimesheetStartResponse,
            skip_block=True,
            requires_instance_id=True,
        )

    def projectTimesheetStop(
        self, request: ProjectTimesheetStopRequest
    ) -> ProjectTimesheetStopResponse:
        return self._invoke(
            "projectTimesheetStop",
            request,
            ProjectTimesheetStopResponse,
            skip_block=True,
            requires_instance_id=True,
        )

    def projectBookingSlotCreate(
        self, request: ProjectBookingSlotCreateRequest
    ) -> ProjectBookingSlotCreateResponse:
        return self._invoke(
            "projectBookingSlotCreate",
            request,
            ProjectBookingSlotCreateResponse,
            skip_block=True,
            requires_instance_id=True,
        )

    def projectBookingBook(
        self, request: ProjectBookingBookRequest
    ) -> ProjectBookingBookResponse:
        return self._invoke(
            "projectBookingBook",
            request,
            ProjectBookingBookResponse,
            skip_block=True,
            requires_instance_id=True,
        )

    def projectBookingCancel(
        self, request: ProjectBookingCancelRequest
    ) -> ProjectBookingCancelResponse:
        return self._invoke(
            "projectBookingCancel",
            request,
            ProjectBookingCancelResponse,
            skip_block=True,
            requires_instance_id=True,
        )

    def projectBookingClose(
        self, request: ProjectBookingCloseRequest
    ) -> ProjectBookingCloseResponse:
        return self._invoke(
            "projectBookingClose",
            request,
            ProjectBookingCloseResponse,
            skip_block=True,
            requires_instance_id=True,
        )

    def projectBookingBookDateRange(
        self, request: ProjectBookingBookDateRangeRequest
    ) -> ProjectBookingBookDateRangeResponse:
        return self._invoke(
            "projectBookingBookDateRange",
            request,
            ProjectBookingBookDateRangeResponse,
            skip_block=True,
            requires_instance_id=True,
        )

    def projectBookingCancelGroup(
        self, request: ProjectBookingCancelGroupRequest
    ) -> ProjectBookingCancelGroupResponse:
        return self._invoke(
            "projectBookingCancelGroup",
            request,
            ProjectBookingCancelGroupResponse,
            skip_block=True,
            requires_instance_id=True,
        )

    def projectBookingCloseGroup(
        self, request: ProjectBookingCloseGroupRequest
    ) -> ProjectBookingCloseGroupResponse:
        return self._invoke(
            "projectBookingCloseGroup",
            request,
            ProjectBookingCloseGroupResponse,
            skip_block=True,
            requires_instance_id=True,
        )

    def projectBookingSetSlotPrice(
        self, request: ProjectBookingSetSlotPriceRequest
    ) -> ProjectBookingSetSlotPriceResponse:
        return self._invoke(
            "projectBookingSetSlotPrice",
            request,
            ProjectBookingSetSlotPriceResponse,
            skip_block=True,
            requires_instance_id=True,
        )

    def projectAvailableSlots(
        self, request: ProjectAvailableSlotsRequest
    ) -> ProjectAvailableSlotsResponse:
        return self._invoke(
            "projectAvailableSlots",
            request,
            ProjectAvailableSlotsResponse,
            skip_block=True,
            requires_instance_id=True,
        )

    def projectWorkerList(
        self, request: Optional[ProjectWorkerListRequest] = None
    ) -> ProjectWorkerListResponse:
        return self._invoke(
            "projectWorkerList",
            request,
            ProjectWorkerListResponse,
            skip_block=True,
            requires_instance_id=True,
        )

    def projectCalendar(
        self, request: ProjectCalendarRequest
    ) -> ProjectCalendarResponse:
        return self._invoke(
            "projectCalendar",
            request,
            ProjectCalendarResponse,
            skip_block=True,
            requires_instance_id=True,
        )

    def projectPassCreate(
        self, request: ProjectPassCreateRequest
    ) -> ProjectPassCreateResponse:
        return self._invoke(
            "projectPassCreate",
            request,
            ProjectPassCreateResponse,
            skip_block=True,
            requires_instance_id=True,
        )

    def projectPassList(
        self, request: ProjectPassListRequest
    ) -> ProjectPassListResponse:
        return self._invoke(
            "projectPassList",
            request,
            ProjectPassListResponse,
            skip_block=True,
            requires_instance_id=True,
        )

    def projectPassDeactivate(
        self, request: ProjectPassDeactivateRequest
    ) -> ProjectPassDeactivateResponse:
        return self._invoke(
            "projectPassDeactivate",
            request,
            ProjectPassDeactivateResponse,
            skip_block=True,
            requires_instance_id=True,
        )

    def projectPassUpdateExpiry(
        self, request: ProjectPassUpdateExpiryRequest
    ) -> ProjectPassUpdateExpiryResponse:
        return self._invoke(
            "projectPassUpdateExpiry",
            request,
            ProjectPassUpdateExpiryResponse,
            skip_block=True,
            requires_instance_id=True,
        )

    def taxList(self, request: TaxListRequest) -> TaxListResponse:
        return self._invoke(
            "taxList",
            request,
            TaxListResponse,
            skip_block=True,
            requires_instance_id=True,
        )

    def taxAdd(self, request: TaxAddRequest) -> TaxAddResponse:
        return self._invoke(
            "taxAdd",
            request,
            TaxAddResponse,
            skip_block=True,
            requires_instance_id=True,
        )

    def taxModify(self, request: TaxModifyRequest) -> TaxModifyResponse:
        return self._invoke(
            "taxModify",
            request,
            TaxModifyResponse,
            skip_block=True,
            requires_instance_id=True,
        )

    def taxActivate(self, request: TaxActivateRequest) -> TaxActivateResponse:
        return self._invoke(
            "taxActivate",
            request,
            TaxActivateResponse,
            skip_block=True,
            requires_instance_id=True,
        )

    def taxInactivate(self, request: TaxInactivateRequest) -> TaxInactivateResponse:
        return self._invoke(
            "taxInactivate",
            request,
            TaxInactivateResponse,
            skip_block=True,
            requires_instance_id=True,
        )

    def paymentModeInactivate(
        self, request: PaymentModeInactivateRequest
    ) -> PaymentModeInactivateResponse:
        return self._invoke(
            "paymentModeInactivate",
            request,
            PaymentModeInactivateResponse,
            skip_block=True,
            requires_instance_id=True,
        )

    def paymentModeActivate(
        self, request: PaymentModeActivateRequest
    ) -> PaymentModeActivateResponse:
        return self._invoke(
            "paymentModeActivate",
            request,
            PaymentModeActivateResponse,
            skip_block=True,
            requires_instance_id=True,
        )

    def paymentModeDownload(
        self, request: Optional[PaymentModeDownloadRequest] = None
    ) -> PaymentModeDownloadResponse:
        return self._invoke(
            "paymentModeDownload",
            request,
            PaymentModeDownloadResponse,
            skip_block=True,
            requires_instance_id=True,
        )

    def orderAdd(self, request: OrderAddRequest) -> OrderAddResponse:
        return self._invoke(
            "orderAdd",
            request,
            OrderAddResponse,
            requires_instance_id=True,
        )

    def orderCollectiveAdd(
        self, request: OrderCollectiveAddRequest
    ) -> OrderCollectiveAddResponse:
        return self._invoke(
            "orderCollectiveAdd",
            request,
            OrderCollectiveAddResponse,
            requires_instance_id=True,
        )

    def orderList(self, request: OrderListRequest) -> OrderListResponse:
        return self._invoke(
            "orderList",
            request,
            OrderListResponse,
            requires_instance_id=True,
            req_mapping={"from_": "from"},
        )

    def orderStorno(self, request: OrderStornoRequest) -> OrderStornoResponse:
        return self._invoke(
            "orderStorno",
            request,
            OrderStornoResponse,
            requires_instance_id=True,
        )

    def orderProformDownload(
        self, request: OrderProformDownloadRequest
    ) -> OrderProformDownloadResponse:
        return self._invoke(
            "orderProformDownload",
            request,
            OrderProformDownloadResponse,
            requires_instance_id=True,
        )

    def orderBill(self, request: OrderBillRequest) -> OrderBillResponse:
        return self._invoke(
            "orderBill",
            request,
            OrderBillResponse,
            requires_instance_id=True,
        )

    def orderDetails(self, request: OrderDetailsRequest) -> OrderDetailsResponse:
        return self._invoke(
            "orderDetails",
            request,
            OrderDetailsResponse,
            requires_instance_id=True,
        )

    def orderCollectiveClose(
        self, request: OrderCollectiveCloseRequest
    ) -> OrderCollectiveCloseResponse:
        return self._invoke(
            "orderCollectiveClose",
            request,
            OrderCollectiveCloseResponse,
            requires_instance_id=True,
        )

    def orderCollectiveSettling(
        self, request: OrderCollectiveSettlingRequest
    ) -> OrderCollectiveSettlingResponse:
        return self._invoke(
            "orderCollectiveSettling",
            request,
            OrderCollectiveSettlingResponse,
            requires_instance_id=True,
        )

    def orderCollectiveAddElements(
        self, request: OrderCollectiveAddElementsRequest
    ) -> OrderCollectiveAddElementsResponse:
        return self._invoke(
            "orderCollectiveAddElements",
            request,
            OrderCollectiveAddElementsResponse,
            requires_instance_id=True,
        )

    def orderSetPaid(self, request: OrderSetPaidRequest) -> OrderSetPaidResponse:
        return self._invoke(
            "orderSetPaid",
            request,
            OrderSetPaidResponse,
            requires_instance_id=True,
        )

    def orderCheckPaid(self, request: OrderCheckPaidRequest) -> OrderCheckPaidResponse:
        return self._invoke(
            "orderCheckPaid",
            request,
            OrderCheckPaidResponse,
            requires_instance_id=True,
        )

    def orderPaidChangeList(
        self, request: Optional[OrderPaidChangeListRequest] = None
    ) -> OrderPaidChangeListResponse:
        return self._invoke(
            "orderPaidChangeList",
            request,
            OrderPaidChangeListResponse,
            requires_instance_id=True,
        )

    def invoiceAdd(self, request: InvoiceAddRequest) -> InvoiceAddResponse:
        return self._invoke(
            "invoiceAdd",
            request,
            InvoiceAddResponse,
            requires_instance_id=True,
        )

    def invoiceAddPrepayment(
        self, request: InvoiceAddPrepaymentRequest
    ) -> InvoiceAddPrepaymentResponse:
        return self._invoke(
            "invoiceAddPrepayment",
            request,
            InvoiceAddPrepaymentResponse,
            requires_instance_id=True,
        )

    def invoiceAddFinal(
        self, request: InvoiceAddFinalRequest
    ) -> InvoiceAddFinalResponse:
        return self._invoke(
            "invoiceAddFinal",
            request,
            InvoiceAddFinalResponse,
            requires_instance_id=True,
        )

    def invoiceDetails(self, request: InvoiceDetailsRequest) -> InvoiceDetailsResponse:
        return self._invoke(
            "invoiceDetails",
            request,
            InvoiceDetailsResponse,
            requires_instance_id=True,
        )

    def invoiceDownload(
        self, request: InvoiceDownloadRequest
    ) -> InvoiceDownloadResponse:
        return self._invoke(
            "invoiceDownload",
            request,
            InvoiceDownloadResponse,
            requires_instance_id=True,
        )

    def invoiceStorno(self, request: InvoiceStornoRequest) -> InvoiceStornoResponse:
        return self._invoke(
            "invoiceStorno",
            request,
            InvoiceStornoResponse,
            requires_instance_id=True,
        )

    def invoiceList(self, request: InvoiceListRequest) -> InvoiceListResponse:
        return self._invoke(
            "invoiceList",
            request,
            InvoiceListResponse,
            requires_instance_id=True,
            req_mapping={"from_": "from"},
        )

    def invoiceExport(self, request: InvoiceExportRequest) -> InvoiceExportResponse:
        return self._invoke(
            "invoiceExport",
            request,
            InvoiceExportResponse,
            requires_instance_id=True,
        )

    def invoiceSearch(self, request: InvoiceSearchRequest) -> InvoiceSearchResponse:
        return self._invoke(
            "invoiceSearch",
            request,
            InvoiceSearchResponse,
            requires_instance_id=True,
        )

    def invoiceCorrection(
        self, request: InvoiceCorrectionRequest
    ) -> InvoiceCorrectionResponse:
        return self._invoke(
            "invoiceCorrection",
            request,
            InvoiceCorrectionResponse,
            skip_block=True,
            requires_instance_id=True,
        )

    def invoiceResend(self, request: InvoiceResendRequest) -> InvoiceResendResponse:
        return self._invoke(
            "invoiceResend",
            request,
            InvoiceResendResponse,
            requires_instance_id=True,
        )

    def invoiceCheckPaid(
        self, request: InvoiceCheckPaidRequest
    ) -> InvoiceCheckPaidResponse:
        return self._invoke(
            "invoiceCheckPaid",
            request,
            InvoiceCheckPaidResponse,
            requires_instance_id=True,
        )

    def invoiceSetPaid(self, request: InvoiceSetPaidRequest) -> InvoiceSetPaidResponse:
        return self._invoke(
            "invoiceSetPaid",
            request,
            InvoiceSetPaidResponse,
            requires_instance_id=True,
        )

    def debtDetails(self, request: DebtDetailsRequest) -> DebtDetailsResponse:
        return self._invoke(
            "debtDetails",
            request,
            DebtDetailsResponse,
            skip_block=True,
            requires_instance_id=True,
        )

    def debtDownload(self, request: DebtDownloadRequest) -> DebtDownloadResponse:
        return self._invoke(
            "debtDownload",
            request,
            DebtDownloadResponse,
            skip_block=True,
            requires_instance_id=True,
        )

    def debtList(self, request: DebtListRequest) -> DebtListResponse:
        return self._invoke(
            "debtList",
            request,
            DebtListResponse,
            skip_block=True,
            requires_instance_id=True,
            req_mapping={"from_": "from"},
        )

    def debtAdd(self, request: DebtAddRequest) -> DebtAddResponse:
        return self._invoke(
            "debtAdd",
            request,
            DebtAddResponse,
            skip_block=True,
            requires_instance_id=True,
        )

    def debtModify(self, request: DebtModifyRequest) -> DebtModifyResponse:
        return self._invoke(
            "debtModify",
            request,
            DebtModifyResponse,
            skip_block=True,
            requires_instance_id=True,
        )

    def debtAccept(self, request: DebtAcceptRequest) -> DebtAcceptResponse:
        return self._invoke(
            "debtAccept",
            request,
            DebtAcceptResponse,
            skip_block=True,
            requires_instance_id=True,
        )

    def debtPay(self, request: DebtPayRequest) -> DebtPayResponse:
        return self._invoke(
            "debtPay",
            request,
            DebtPayResponse,
            skip_block=True,
            requires_instance_id=True,
        )

    def debtDelete(self, request: DebtDeleteRequest) -> DebtDeleteResponse:
        return self._invoke(
            "debtDelete",
            request,
            DebtDeleteResponse,
            skip_block=True,
            requires_instance_id=True,
        )

    def debtGenerate(self, request: DebtGenerateRequest) -> DebtGenerateResponse:
        return self._invoke(
            "debtGenerate",
            request,
            DebtGenerateResponse,
            skip_block=True,
            requires_instance_id=True,
        )

    def debtExport(self, request: DebtExportRequest) -> DebtExportResponse:
        return self._invoke(
            "debtExport",
            request,
            DebtExportResponse,
            skip_block=True,
            requires_instance_id=True,
        )

    def systemMessageList(
        self, request: Optional[SystemMessageListRequest] = None
    ) -> SystemMessageListResponse:
        return self._invoke(
            "systemMessageList",
            request,
            SystemMessageListResponse,
            skip_block=True,
            requires_instance_id=True,
        )

    def systemMessageSetRead(
        self, request: SystemMessageSetReadRequest
    ) -> SystemMessageSetReadResponse:
        return self._invoke(
            "systemMessageSetRead",
            request,
            SystemMessageSetReadResponse,
            skip_block=True,
            requires_instance_id=True,
        )

    def systemErrorCodeList(
        self, request: SystemErrorCodeListRequest
    ) -> SystemErrorCodeListResponse:
        return self._invoke(
            "systemErrorCodeList",
            request,
            SystemErrorCodeListResponse,
            skip_block=True,
            requires_instance_id=True,
        )

    def getVersion(
        self, request: Optional[GetVersionRequest] = None
    ) -> GetVersionResponse:
        return self._invoke(
            "getVersion",
            request,
            GetVersionResponse,
            skip_block=True,
            requires_instance_id=True,
        )

    def serviceProviderDatas(
        self, request: Optional[ServiceProviderDatasRequest] = None
    ) -> ServiceProviderDatasResponse:
        return self._invoke(
            "serviceProviderDatas",
            request,
            ServiceProviderDatasResponse,
            skip_block=True,
            requires_instance_id=True,
        )

    def companyData(
        self, request: Optional[CompanyDataRequest] = None
    ) -> CompanyDataResponse:
        return self._invoke(
            "companyData",
            request,
            CompanyDataResponse,
            skip_block=True,
            requires_instance_id=True,
        )

    def quantityList(self, request: QuantityListRequest) -> QuantityListResponse:
        return self._invoke(
            "quantityList",
            request,
            QuantityListResponse,
            skip_block=True,
            requires_instance_id=True,
        )

    def currencyDownload(
        self, request: CurrencyDownloadRequest
    ) -> CurrencyDownloadResponse:
        return self._invoke(
            "currencyDownload",
            request,
            CurrencyDownloadResponse,
            skip_block=True,
            requires_instance_id=True,
        )

    def regularityDownload(
        self, request: Optional[RegularityDownloadRequest] = None
    ) -> RegularityDownloadResponse:
        return self._invoke(
            "regularityDownload",
            request,
            RegularityDownloadResponse,
            skip_block=True,
            requires_instance_id=True,
        )

    def countryDownload(
        self, request: Optional[CountryDownloadRequest] = None
    ) -> CountryDownloadResponse:
        return self._invoke(
            "countryDownload",
            request,
            CountryDownloadResponse,
            skip_block=True,
            requires_instance_id=True,
        )

    def postcodeDownload(
        self, request: PostcodeDownloadRequest
    ) -> PostcodeDownloadResponse:
        return self._invoke(
            "postcodeDownload",
            request,
            PostcodeDownloadResponse,
            skip_block=True,
            requires_instance_id=True,
        )

    def ping(self, request: Optional[PingRequest] = None) -> PingResponse:
        return self._invoke(
            "ping",
            request,
            PingResponse,
            skip_block=True,
            requires_instance_id=True,
        )

    def monitor(self, request: Optional[MonitorRequest] = None) -> MonitorResponse:
        return self._invoke(
            "monitor",
            request,
            MonitorResponse,
            skip_block=True,
            requires_instance_id=True,
        )
