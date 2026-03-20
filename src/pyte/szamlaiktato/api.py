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
    instance_id: str
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
    instance_id: str
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
    instance_id: str
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
    instance_id: str
    sid: str


@dataclass
class CustomerActivateResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    sid: Optional[str] = None


@dataclass
class CustomerInactivateRequest:
    instance_id: str
    sid: str


@dataclass
class CustomerInactivateResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    sid: Optional[str] = None


@dataclass
class CustomerSwapRequest:
    instance_id: str
    sid: str
    swapped_sids: builtins.list[builtins.dict[str, Any]]


@dataclass
class CustomerSwapResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    sid: Optional[str] = None


@dataclass
class CustomerListRequest:
    instance_id: str
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
    instance_id: str
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
    instance_id: str
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
    instance_id: str
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
    instance_id: str
    sid: str


@dataclass
class ProductActivateResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    sid: Optional[str] = None


@dataclass
class ProductInactivateRequest:
    instance_id: str
    sid: str


@dataclass
class ProductInactivateResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    sid: Optional[str] = None


@dataclass
class ProductListRequest:
    instance_id: str
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
    instance_id: str
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
    instance_id: str


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
    instance_id: str
    type: str


@dataclass
class OuterDatasourcesGetResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    data: Optional[str] = None


@dataclass
class OuterDatasourcesSaveRequest:
    instance_id: str
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
    instance_id: str
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
    instance_id: str
    email: str
    new_password: str


@dataclass
class AdminUserPasswordResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    email: Optional[str] = None


@dataclass
class AdminUserDelRequest:
    instance_id: str
    email: str


@dataclass
class AdminUserDelResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    email: Optional[str] = None


@dataclass
class BlockAddRequest:
    instance_id: str
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
    instance_id: str
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
    instance_id: str
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
    instance_id: str
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
    instance_id: str
    block_id: int
    block_name: str


@dataclass
class BlockCloseResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None


@dataclass
class BlockOpenRequest:
    instance_id: str
    block_id: int
    block_name: str


@dataclass
class BlockOpenResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None


@dataclass
class CostCentreAddRequest:
    instance_id: str
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
    instance_id: str
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
    instance_id: str


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
    instance_id: str
    code: str


@dataclass
class CostCentreActivateResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    code: Optional[str] = None


@dataclass
class CostCentreInactivateRequest:
    instance_id: str
    code: str


@dataclass
class CostCentreInactivateResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    code: Optional[str] = None


@dataclass
class CostTypeAddRequest:
    instance_id: str
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
    instance_id: str
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
    instance_id: str


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
    instance_id: str
    code: str


@dataclass
class CostTypeActivateResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    code: Optional[str] = None


@dataclass
class CostTypeInactivateRequest:
    instance_id: str
    code: str


@dataclass
class CostTypeInactivateResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    code: Optional[str] = None


@dataclass
class ProjectListRequest:
    instance_id: Optional[str] = None
    active: Optional[int] = None


@dataclass
class ProjectListResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    projects: Optional[builtins.list[builtins.dict[str, Any]]] = None


@dataclass
class ProjectGetRequest:
    code: str
    instance_id: Optional[str] = None


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
    instance_id: Optional[str] = None
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
    instance_id: Optional[str] = None


@dataclass
class ProjectInactivateResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    code: Optional[str] = None


@dataclass
class ProjectTimesheetListRequest:
    code: str
    instance_id: Optional[str] = None


@dataclass
class ProjectTimesheetListResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    timesheets: Optional[builtins.list[builtins.dict[str, Any]]] = None


@dataclass
class ProjectTimesheetStartRequest:
    code: str
    projects_workers_id: int
    instance_id: Optional[str] = None
    comment: Optional[str] = None


@dataclass
class ProjectTimesheetStartResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    timesheet_id: Optional[int] = None


@dataclass
class ProjectTimesheetStopRequest:
    timesheet_id: int
    instance_id: Optional[str] = None
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
    instance_id: Optional[str] = None
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
    instance_id: Optional[str] = None


@dataclass
class ProjectBookingBookResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    timesheet_id: Optional[int] = None


@dataclass
class ProjectBookingCancelRequest:
    timesheet_id: int
    instance_id: Optional[str] = None


@dataclass
class ProjectBookingCancelResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    timesheet_id: Optional[int] = None


@dataclass
class ProjectBookingCloseRequest:
    timesheet_id: int
    instance_id: Optional[str] = None


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
    instance_id: Optional[str] = None


@dataclass
class ProjectBookingBookDateRangeResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    booking_group_id: Optional[str] = None
    nights: Optional[int] = None


@dataclass
class ProjectBookingCancelGroupRequest:
    booking_group_id: str
    instance_id: Optional[str] = None


@dataclass
class ProjectBookingCancelGroupResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    booking_group_id: Optional[str] = None


@dataclass
class ProjectBookingCloseGroupRequest:
    booking_group_id: str
    instance_id: Optional[str] = None
    comment: Optional[str] = None


@dataclass
class ProjectBookingCloseGroupResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    booking_group_id: Optional[str] = None


@dataclass
class ProjectBookingSetSlotPriceRequest:
    timesheet_id: int
    instance_id: Optional[str] = None
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
    instance_id: Optional[str] = None


@dataclass
class ProjectAvailableSlotsResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    slots: Optional[builtins.list[builtins.dict[str, Any]]] = None


@dataclass
class ProjectWorkerListRequest:
    instance_id: Optional[str] = None


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
    instance_id: Optional[str] = None


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
    instance_id: Optional[str] = None
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
    instance_id: Optional[str] = None


@dataclass
class ProjectPassListResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    passes: Optional[builtins.list[builtins.dict[str, Any]]] = None


@dataclass
class ProjectPassDeactivateRequest:
    pass_id: int
    instance_id: Optional[str] = None


@dataclass
class ProjectPassDeactivateResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None


@dataclass
class ProjectPassUpdateExpiryRequest:
    pass_id: int
    expiry_date: str
    instance_id: Optional[str] = None


@dataclass
class ProjectPassUpdateExpiryResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None


@dataclass
class TaxListRequest:
    instance_id: str
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
    instance_id: str
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
    instance_id: str
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
    instance_id: str
    code: str


@dataclass
class TaxActivateResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    code: Optional[str] = None


@dataclass
class TaxInactivateRequest:
    instance_id: str
    code: str


@dataclass
class TaxInactivateResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    code: Optional[str] = None


@dataclass
class PaymentModeInactivateRequest:
    instance_id: str
    code: str


@dataclass
class PaymentModeInactivateResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None


@dataclass
class PaymentModeActivateRequest:
    instance_id: str
    code: str


@dataclass
class PaymentModeActivateResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None


@dataclass
class PaymentModeDownloadRequest:
    instance_id: str


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
    instance_id: str
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
    instance_id: str
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
    instance_id: str
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
    instance_id: str
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
    instance_id: str
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
    instance_id: str
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
    instance_id: str
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
    instance_id: str
    customer_sid: str


@dataclass
class OrderCollectiveCloseResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    invoice_number: Optional[str] = None


@dataclass
class OrderCollectiveSettlingRequest:
    instance_id: str
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
    instance_id: str
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
    instance_id: str
    order_number: str


@dataclass
class OrderSetPaidResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    paid: Optional[int] = None
    paid_code: Optional[str] = None


@dataclass
class OrderCheckPaidRequest:
    instance_id: str
    order_number: str


@dataclass
class OrderCheckPaidResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    paid: Optional[int] = None
    paid_code: Optional[str] = None


@dataclass
class OrderPaidChangeListRequest:
    instance_id: str


@dataclass
class OrderPaidChangeListResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    list: Optional[builtins.list[builtins.dict[str, Any]]] = None
    order_number: Optional[str] = None


@dataclass
class InvoiceAddRequest:
    instance_id: str
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
    instance_id: str
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
    instance_id: str
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
    instance_id: str
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
    instance_id: str
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
    instance_id: str
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
    instance_id: str
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
    instance_id: str
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
    instance_id: str
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
    instance_id: str
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
    instance_id: str
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
    instance_id: str
    invoice_number: str


@dataclass
class InvoiceCheckPaidResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    paid: Optional[int] = None
    paid_code: Optional[str] = None


@dataclass
class InvoiceSetPaidRequest:
    instance_id: str
    invoice_number: str


@dataclass
class InvoiceSetPaidResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    paid: Optional[int] = None
    paid_code: Optional[str] = None


@dataclass
class DebtDetailsRequest:
    instance_id: str
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
    instance_id: str
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
    instance_id: str
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
    instance_id: str
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
    instance_id: str
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
    instance_id: str
    debt_ids: builtins.list[builtins.dict[str, Any]]


@dataclass
class DebtAcceptResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    accepted_count: Optional[int] = None


@dataclass
class DebtPayRequest:
    instance_id: str
    debt_ids: builtins.list[builtins.dict[str, Any]]


@dataclass
class DebtPayResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    paid_count: Optional[int] = None


@dataclass
class DebtDeleteRequest:
    instance_id: str
    debt_ids: builtins.list[builtins.dict[str, Any]]


@dataclass
class DebtDeleteResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    deleted_count: Optional[int] = None


@dataclass
class DebtGenerateRequest:
    instance_id: str
    debt_ids: builtins.list[builtins.dict[str, Any]]


@dataclass
class DebtGenerateResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    file: Optional[str] = None
    file_size: Optional[int] = None


@dataclass
class DebtExportRequest:
    instance_id: str
    dateFrom: str
    dateTo: str


@dataclass
class DebtExportResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    list: Optional[builtins.list[builtins.dict[str, Any]]] = None


@dataclass
class SystemMessageListRequest:
    instance_id: str


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
    instance_id: str
    id: int


@dataclass
class SystemMessageSetReadResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None


@dataclass
class SystemErrorCodeListRequest:
    instance_id: str
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
    instance_id: str


@dataclass
class GetVersionResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    version: Optional[str] = None


@dataclass
class ServiceProviderDatasRequest:
    instance_id: str


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
    instance_id: str


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
    instance_id: str
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
    instance_id: str
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
    instance_id: str


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
    instance_id: str


@dataclass
class CountryDownloadResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None
    list: Optional[builtins.list[builtins.dict[str, Any]]] = None
    code: Optional[str] = None
    country: Optional[str] = None


@dataclass
class PostcodeDownloadRequest:
    instance_id: str
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
    instance_id: str


@dataclass
class PingResponse:
    status_id: Optional[int] = None
    status: Optional[str] = None


@dataclass
class MonitorRequest:
    instance_id: str


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
        skip_block: bool,
        req_mapping: builtins.dict[str, str],
        resp_mapping: builtins.dict[str, str],
    ) -> Any:
        params = asdict(request) if request else {}
        for py_name, orig_name in req_mapping.items():
            if py_name in params:
                params[orig_name] = params.pop(py_name)
        data = self.client._call(method, params, skip_block=skip_block)
        for orig_name, py_name in resp_mapping.items():
            if orig_name in data:
                data[py_name] = data.pop(orig_name)
        valid_keys = response_cls.__dataclass_fields__.keys()
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return response_cls(**filtered_data)

    def install(self, request: InstallRequest) -> InstallResponse:
        return self._invoke(
            method="install",
            request=request,
            response_cls=InstallResponse,
            skip_block=True,
            req_mapping={},
            resp_mapping={},
        )

    def update(self, request: UpdateRequest) -> UpdateResponse:
        return self._invoke(
            method="update",
            request=request,
            response_cls=UpdateResponse,
            skip_block=True,
            req_mapping={},
            resp_mapping={},
        )

    def customerAdd(self, request: CustomerAddRequest) -> CustomerAddResponse:
        return self._invoke(
            method="customerAdd",
            request=request,
            response_cls=CustomerAddResponse,
            skip_block=False,
            req_mapping={},
            resp_mapping={},
        )

    def customerModify(self, request: CustomerModifyRequest) -> CustomerModifyResponse:
        return self._invoke(
            method="customerModify",
            request=request,
            response_cls=CustomerModifyResponse,
            skip_block=False,
            req_mapping={},
            resp_mapping={},
        )

    def customerGet(self, request: CustomerGetRequest) -> CustomerGetResponse:
        return self._invoke(
            method="customerGet",
            request=request,
            response_cls=CustomerGetResponse,
            skip_block=False,
            req_mapping={},
            resp_mapping={},
        )

    def customerActivate(
        self, request: CustomerActivateRequest
    ) -> CustomerActivateResponse:
        return self._invoke(
            method="customerActivate",
            request=request,
            response_cls=CustomerActivateResponse,
            skip_block=False,
            req_mapping={},
            resp_mapping={},
        )

    def customerInactivate(
        self, request: CustomerInactivateRequest
    ) -> CustomerInactivateResponse:
        return self._invoke(
            method="customerInactivate",
            request=request,
            response_cls=CustomerInactivateResponse,
            skip_block=False,
            req_mapping={},
            resp_mapping={},
        )

    def customerSwap(self, request: CustomerSwapRequest) -> CustomerSwapResponse:
        return self._invoke(
            method="customerSwap",
            request=request,
            response_cls=CustomerSwapResponse,
            skip_block=False,
            req_mapping={},
            resp_mapping={},
        )

    def customerList(self, request: CustomerListRequest) -> CustomerListResponse:
        return self._invoke(
            method="customerList",
            request=request,
            response_cls=CustomerListResponse,
            skip_block=True,
            req_mapping={},
            resp_mapping={},
        )

    def productAdd(self, request: ProductAddRequest) -> ProductAddResponse:
        return self._invoke(
            method="productAdd",
            request=request,
            response_cls=ProductAddResponse,
            skip_block=False,
            req_mapping={},
            resp_mapping={},
        )

    def productModify(self, request: ProductModifyRequest) -> ProductModifyResponse:
        return self._invoke(
            method="productModify",
            request=request,
            response_cls=ProductModifyResponse,
            skip_block=False,
            req_mapping={},
            resp_mapping={},
        )

    def productGet(self, request: ProductGetRequest) -> ProductGetResponse:
        return self._invoke(
            method="productGet",
            request=request,
            response_cls=ProductGetResponse,
            skip_block=False,
            req_mapping={},
            resp_mapping={},
        )

    def productActivate(
        self, request: ProductActivateRequest
    ) -> ProductActivateResponse:
        return self._invoke(
            method="productActivate",
            request=request,
            response_cls=ProductActivateResponse,
            skip_block=False,
            req_mapping={},
            resp_mapping={},
        )

    def productInactivate(
        self, request: ProductInactivateRequest
    ) -> ProductInactivateResponse:
        return self._invoke(
            method="productInactivate",
            request=request,
            response_cls=ProductInactivateResponse,
            skip_block=False,
            req_mapping={},
            resp_mapping={},
        )

    def productList(self, request: ProductListRequest) -> ProductListResponse:
        return self._invoke(
            method="productList",
            request=request,
            response_cls=ProductListResponse,
            skip_block=True,
            req_mapping={},
            resp_mapping={},
        )

    def productFileList(
        self, request: ProductFileListRequest
    ) -> ProductFileListResponse:
        return self._invoke(
            method="productFileList",
            request=request,
            response_cls=ProductFileListResponse,
            skip_block=True,
            req_mapping={},
            resp_mapping={},
        )

    def outerDatasources(
        self, request: OuterDatasourcesRequest
    ) -> OuterDatasourcesResponse:
        return self._invoke(
            method="outerDatasources",
            request=request,
            response_cls=OuterDatasourcesResponse,
            skip_block=True,
            req_mapping={},
            resp_mapping={},
        )

    def outerDatasourcesGet(
        self, request: OuterDatasourcesGetRequest
    ) -> OuterDatasourcesGetResponse:
        return self._invoke(
            method="outerDatasourcesGet",
            request=request,
            response_cls=OuterDatasourcesGetResponse,
            skip_block=True,
            req_mapping={},
            resp_mapping={},
        )

    def outerDatasourcesSave(
        self, request: OuterDatasourcesSaveRequest
    ) -> OuterDatasourcesSaveResponse:
        return self._invoke(
            method="outerDatasourcesSave",
            request=request,
            response_cls=OuterDatasourcesSaveResponse,
            skip_block=True,
            req_mapping={},
            resp_mapping={},
        )

    def adminUserAdd(self, request: AdminUserAddRequest) -> AdminUserAddResponse:
        return self._invoke(
            method="adminUserAdd",
            request=request,
            response_cls=AdminUserAddResponse,
            skip_block=True,
            req_mapping={},
            resp_mapping={},
        )

    def adminUserPassword(
        self, request: AdminUserPasswordRequest
    ) -> AdminUserPasswordResponse:
        return self._invoke(
            method="adminUserPassword",
            request=request,
            response_cls=AdminUserPasswordResponse,
            skip_block=True,
            req_mapping={},
            resp_mapping={},
        )

    def adminUserDel(self, request: AdminUserDelRequest) -> AdminUserDelResponse:
        return self._invoke(
            method="adminUserDel",
            request=request,
            response_cls=AdminUserDelResponse,
            skip_block=True,
            req_mapping={},
            resp_mapping={},
        )

    def blockAdd(self, request: BlockAddRequest) -> BlockAddResponse:
        return self._invoke(
            method="blockAdd",
            request=request,
            response_cls=BlockAddResponse,
            skip_block=True,
            req_mapping={},
            resp_mapping={},
        )

    def blockUpdateCompanyData(
        self, request: BlockUpdateCompanyDataRequest
    ) -> BlockUpdateCompanyDataResponse:
        return self._invoke(
            method="blockUpdateCompanyData",
            request=request,
            response_cls=BlockUpdateCompanyDataResponse,
            skip_block=True,
            req_mapping={},
            resp_mapping={},
        )

    def blockModify(self, request: BlockModifyRequest) -> BlockModifyResponse:
        return self._invoke(
            method="blockModify",
            request=request,
            response_cls=BlockModifyResponse,
            skip_block=True,
            req_mapping={},
            resp_mapping={},
        )

    def blockList(self, request: BlockListRequest) -> BlockListResponse:
        return self._invoke(
            method="blockList",
            request=request,
            response_cls=BlockListResponse,
            skip_block=True,
            req_mapping={},
            resp_mapping={},
        )

    def blockClose(self, request: BlockCloseRequest) -> BlockCloseResponse:
        return self._invoke(
            method="blockClose",
            request=request,
            response_cls=BlockCloseResponse,
            skip_block=True,
            req_mapping={},
            resp_mapping={},
        )

    def blockOpen(self, request: BlockOpenRequest) -> BlockOpenResponse:
        return self._invoke(
            method="blockOpen",
            request=request,
            response_cls=BlockOpenResponse,
            skip_block=True,
            req_mapping={},
            resp_mapping={},
        )

    def costCentreAdd(self, request: CostCentreAddRequest) -> CostCentreAddResponse:
        return self._invoke(
            method="costCentreAdd",
            request=request,
            response_cls=CostCentreAddResponse,
            skip_block=True,
            req_mapping={},
            resp_mapping={},
        )

    def costCentreModify(
        self, request: CostCentreModifyRequest
    ) -> CostCentreModifyResponse:
        return self._invoke(
            method="costCentreModify",
            request=request,
            response_cls=CostCentreModifyResponse,
            skip_block=True,
            req_mapping={},
            resp_mapping={},
        )

    def costCentreList(self, request: CostCentreListRequest) -> CostCentreListResponse:
        return self._invoke(
            method="costCentreList",
            request=request,
            response_cls=CostCentreListResponse,
            skip_block=True,
            req_mapping={},
            resp_mapping={},
        )

    def costCentreActivate(
        self, request: CostCentreActivateRequest
    ) -> CostCentreActivateResponse:
        return self._invoke(
            method="costCentreActivate",
            request=request,
            response_cls=CostCentreActivateResponse,
            skip_block=True,
            req_mapping={},
            resp_mapping={},
        )

    def costCentreInactivate(
        self, request: CostCentreInactivateRequest
    ) -> CostCentreInactivateResponse:
        return self._invoke(
            method="costCentreInactivate",
            request=request,
            response_cls=CostCentreInactivateResponse,
            skip_block=True,
            req_mapping={},
            resp_mapping={},
        )

    def costTypeAdd(self, request: CostTypeAddRequest) -> CostTypeAddResponse:
        return self._invoke(
            method="costTypeAdd",
            request=request,
            response_cls=CostTypeAddResponse,
            skip_block=True,
            req_mapping={},
            resp_mapping={},
        )

    def costTypeModify(self, request: CostTypeModifyRequest) -> CostTypeModifyResponse:
        return self._invoke(
            method="costTypeModify",
            request=request,
            response_cls=CostTypeModifyResponse,
            skip_block=True,
            req_mapping={},
            resp_mapping={},
        )

    def costTypeList(self, request: CostTypeListRequest) -> CostTypeListResponse:
        return self._invoke(
            method="costTypeList",
            request=request,
            response_cls=CostTypeListResponse,
            skip_block=True,
            req_mapping={},
            resp_mapping={},
        )

    def costTypeActivate(
        self, request: CostTypeActivateRequest
    ) -> CostTypeActivateResponse:
        return self._invoke(
            method="costTypeActivate",
            request=request,
            response_cls=CostTypeActivateResponse,
            skip_block=True,
            req_mapping={},
            resp_mapping={},
        )

    def costTypeInactivate(
        self, request: CostTypeInactivateRequest
    ) -> CostTypeInactivateResponse:
        return self._invoke(
            method="costTypeInactivate",
            request=request,
            response_cls=CostTypeInactivateResponse,
            skip_block=True,
            req_mapping={},
            resp_mapping={},
        )

    def projectList(self, request: ProjectListRequest) -> ProjectListResponse:
        return self._invoke(
            method="projectList",
            request=request,
            response_cls=ProjectListResponse,
            skip_block=True,
            req_mapping={},
            resp_mapping={},
        )

    def projectGet(self, request: ProjectGetRequest) -> ProjectGetResponse:
        return self._invoke(
            method="projectGet",
            request=request,
            response_cls=ProjectGetResponse,
            skip_block=True,
            req_mapping={},
            resp_mapping={},
        )

    def projectCreate(self, request: ProjectCreateRequest) -> ProjectCreateResponse:
        return self._invoke(
            method="projectCreate",
            request=request,
            response_cls=ProjectCreateResponse,
            skip_block=True,
            req_mapping={},
            resp_mapping={},
        )

    def projectInactivate(
        self, request: ProjectInactivateRequest
    ) -> ProjectInactivateResponse:
        return self._invoke(
            method="projectInactivate",
            request=request,
            response_cls=ProjectInactivateResponse,
            skip_block=True,
            req_mapping={},
            resp_mapping={},
        )

    def projectTimesheetList(
        self, request: ProjectTimesheetListRequest
    ) -> ProjectTimesheetListResponse:
        return self._invoke(
            method="projectTimesheetList",
            request=request,
            response_cls=ProjectTimesheetListResponse,
            skip_block=True,
            req_mapping={},
            resp_mapping={},
        )

    def projectTimesheetStart(
        self, request: ProjectTimesheetStartRequest
    ) -> ProjectTimesheetStartResponse:
        return self._invoke(
            method="projectTimesheetStart",
            request=request,
            response_cls=ProjectTimesheetStartResponse,
            skip_block=True,
            req_mapping={},
            resp_mapping={},
        )

    def projectTimesheetStop(
        self, request: ProjectTimesheetStopRequest
    ) -> ProjectTimesheetStopResponse:
        return self._invoke(
            method="projectTimesheetStop",
            request=request,
            response_cls=ProjectTimesheetStopResponse,
            skip_block=True,
            req_mapping={},
            resp_mapping={},
        )

    def projectBookingSlotCreate(
        self, request: ProjectBookingSlotCreateRequest
    ) -> ProjectBookingSlotCreateResponse:
        return self._invoke(
            method="projectBookingSlotCreate",
            request=request,
            response_cls=ProjectBookingSlotCreateResponse,
            skip_block=True,
            req_mapping={},
            resp_mapping={},
        )

    def projectBookingBook(
        self, request: ProjectBookingBookRequest
    ) -> ProjectBookingBookResponse:
        return self._invoke(
            method="projectBookingBook",
            request=request,
            response_cls=ProjectBookingBookResponse,
            skip_block=True,
            req_mapping={},
            resp_mapping={},
        )

    def projectBookingCancel(
        self, request: ProjectBookingCancelRequest
    ) -> ProjectBookingCancelResponse:
        return self._invoke(
            method="projectBookingCancel",
            request=request,
            response_cls=ProjectBookingCancelResponse,
            skip_block=True,
            req_mapping={},
            resp_mapping={},
        )

    def projectBookingClose(
        self, request: ProjectBookingCloseRequest
    ) -> ProjectBookingCloseResponse:
        return self._invoke(
            method="projectBookingClose",
            request=request,
            response_cls=ProjectBookingCloseResponse,
            skip_block=True,
            req_mapping={},
            resp_mapping={},
        )

    def projectBookingBookDateRange(
        self, request: ProjectBookingBookDateRangeRequest
    ) -> ProjectBookingBookDateRangeResponse:
        return self._invoke(
            method="projectBookingBookDateRange",
            request=request,
            response_cls=ProjectBookingBookDateRangeResponse,
            skip_block=True,
            req_mapping={},
            resp_mapping={},
        )

    def projectBookingCancelGroup(
        self, request: ProjectBookingCancelGroupRequest
    ) -> ProjectBookingCancelGroupResponse:
        return self._invoke(
            method="projectBookingCancelGroup",
            request=request,
            response_cls=ProjectBookingCancelGroupResponse,
            skip_block=True,
            req_mapping={},
            resp_mapping={},
        )

    def projectBookingCloseGroup(
        self, request: ProjectBookingCloseGroupRequest
    ) -> ProjectBookingCloseGroupResponse:
        return self._invoke(
            method="projectBookingCloseGroup",
            request=request,
            response_cls=ProjectBookingCloseGroupResponse,
            skip_block=True,
            req_mapping={},
            resp_mapping={},
        )

    def projectBookingSetSlotPrice(
        self, request: ProjectBookingSetSlotPriceRequest
    ) -> ProjectBookingSetSlotPriceResponse:
        return self._invoke(
            method="projectBookingSetSlotPrice",
            request=request,
            response_cls=ProjectBookingSetSlotPriceResponse,
            skip_block=True,
            req_mapping={},
            resp_mapping={},
        )

    def projectAvailableSlots(
        self, request: ProjectAvailableSlotsRequest
    ) -> ProjectAvailableSlotsResponse:
        return self._invoke(
            method="projectAvailableSlots",
            request=request,
            response_cls=ProjectAvailableSlotsResponse,
            skip_block=True,
            req_mapping={},
            resp_mapping={},
        )

    def projectWorkerList(
        self, request: ProjectWorkerListRequest
    ) -> ProjectWorkerListResponse:
        return self._invoke(
            method="projectWorkerList",
            request=request,
            response_cls=ProjectWorkerListResponse,
            skip_block=True,
            req_mapping={},
            resp_mapping={},
        )

    def projectCalendar(
        self, request: ProjectCalendarRequest
    ) -> ProjectCalendarResponse:
        return self._invoke(
            method="projectCalendar",
            request=request,
            response_cls=ProjectCalendarResponse,
            skip_block=True,
            req_mapping={},
            resp_mapping={},
        )

    def projectPassCreate(
        self, request: ProjectPassCreateRequest
    ) -> ProjectPassCreateResponse:
        return self._invoke(
            method="projectPassCreate",
            request=request,
            response_cls=ProjectPassCreateResponse,
            skip_block=True,
            req_mapping={},
            resp_mapping={},
        )

    def projectPassList(
        self, request: ProjectPassListRequest
    ) -> ProjectPassListResponse:
        return self._invoke(
            method="projectPassList",
            request=request,
            response_cls=ProjectPassListResponse,
            skip_block=True,
            req_mapping={},
            resp_mapping={},
        )

    def projectPassDeactivate(
        self, request: ProjectPassDeactivateRequest
    ) -> ProjectPassDeactivateResponse:
        return self._invoke(
            method="projectPassDeactivate",
            request=request,
            response_cls=ProjectPassDeactivateResponse,
            skip_block=True,
            req_mapping={},
            resp_mapping={},
        )

    def projectPassUpdateExpiry(
        self, request: ProjectPassUpdateExpiryRequest
    ) -> ProjectPassUpdateExpiryResponse:
        return self._invoke(
            method="projectPassUpdateExpiry",
            request=request,
            response_cls=ProjectPassUpdateExpiryResponse,
            skip_block=True,
            req_mapping={},
            resp_mapping={},
        )

    def taxList(self, request: TaxListRequest) -> TaxListResponse:
        return self._invoke(
            method="taxList",
            request=request,
            response_cls=TaxListResponse,
            skip_block=True,
            req_mapping={},
            resp_mapping={},
        )

    def taxAdd(self, request: TaxAddRequest) -> TaxAddResponse:
        return self._invoke(
            method="taxAdd",
            request=request,
            response_cls=TaxAddResponse,
            skip_block=True,
            req_mapping={},
            resp_mapping={},
        )

    def taxModify(self, request: TaxModifyRequest) -> TaxModifyResponse:
        return self._invoke(
            method="taxModify",
            request=request,
            response_cls=TaxModifyResponse,
            skip_block=True,
            req_mapping={},
            resp_mapping={},
        )

    def taxActivate(self, request: TaxActivateRequest) -> TaxActivateResponse:
        return self._invoke(
            method="taxActivate",
            request=request,
            response_cls=TaxActivateResponse,
            skip_block=True,
            req_mapping={},
            resp_mapping={},
        )

    def taxInactivate(self, request: TaxInactivateRequest) -> TaxInactivateResponse:
        return self._invoke(
            method="taxInactivate",
            request=request,
            response_cls=TaxInactivateResponse,
            skip_block=True,
            req_mapping={},
            resp_mapping={},
        )

    def paymentModeInactivate(
        self, request: PaymentModeInactivateRequest
    ) -> PaymentModeInactivateResponse:
        return self._invoke(
            method="paymentModeInactivate",
            request=request,
            response_cls=PaymentModeInactivateResponse,
            skip_block=True,
            req_mapping={},
            resp_mapping={},
        )

    def paymentModeActivate(
        self, request: PaymentModeActivateRequest
    ) -> PaymentModeActivateResponse:
        return self._invoke(
            method="paymentModeActivate",
            request=request,
            response_cls=PaymentModeActivateResponse,
            skip_block=True,
            req_mapping={},
            resp_mapping={},
        )

    def paymentModeDownload(
        self, request: PaymentModeDownloadRequest
    ) -> PaymentModeDownloadResponse:
        return self._invoke(
            method="paymentModeDownload",
            request=request,
            response_cls=PaymentModeDownloadResponse,
            skip_block=True,
            req_mapping={},
            resp_mapping={},
        )

    def orderAdd(self, request: OrderAddRequest) -> OrderAddResponse:
        return self._invoke(
            method="orderAdd",
            request=request,
            response_cls=OrderAddResponse,
            skip_block=False,
            req_mapping={},
            resp_mapping={},
        )

    def orderCollectiveAdd(
        self, request: OrderCollectiveAddRequest
    ) -> OrderCollectiveAddResponse:
        return self._invoke(
            method="orderCollectiveAdd",
            request=request,
            response_cls=OrderCollectiveAddResponse,
            skip_block=False,
            req_mapping={},
            resp_mapping={},
        )

    def orderList(self, request: OrderListRequest) -> OrderListResponse:
        return self._invoke(
            method="orderList",
            request=request,
            response_cls=OrderListResponse,
            skip_block=False,
            req_mapping={"from_": "from"},
            resp_mapping={},
        )

    def orderStorno(self, request: OrderStornoRequest) -> OrderStornoResponse:
        return self._invoke(
            method="orderStorno",
            request=request,
            response_cls=OrderStornoResponse,
            skip_block=False,
            req_mapping={},
            resp_mapping={},
        )

    def orderProformDownload(
        self, request: OrderProformDownloadRequest
    ) -> OrderProformDownloadResponse:
        return self._invoke(
            method="orderProformDownload",
            request=request,
            response_cls=OrderProformDownloadResponse,
            skip_block=False,
            req_mapping={},
            resp_mapping={},
        )

    def orderBill(self, request: OrderBillRequest) -> OrderBillResponse:
        return self._invoke(
            method="orderBill",
            request=request,
            response_cls=OrderBillResponse,
            skip_block=False,
            req_mapping={},
            resp_mapping={},
        )

    def orderDetails(self, request: OrderDetailsRequest) -> OrderDetailsResponse:
        return self._invoke(
            method="orderDetails",
            request=request,
            response_cls=OrderDetailsResponse,
            skip_block=False,
            req_mapping={},
            resp_mapping={},
        )

    def orderCollectiveClose(
        self, request: OrderCollectiveCloseRequest
    ) -> OrderCollectiveCloseResponse:
        return self._invoke(
            method="orderCollectiveClose",
            request=request,
            response_cls=OrderCollectiveCloseResponse,
            skip_block=False,
            req_mapping={},
            resp_mapping={},
        )

    def orderCollectiveSettling(
        self, request: OrderCollectiveSettlingRequest
    ) -> OrderCollectiveSettlingResponse:
        return self._invoke(
            method="orderCollectiveSettling",
            request=request,
            response_cls=OrderCollectiveSettlingResponse,
            skip_block=False,
            req_mapping={},
            resp_mapping={},
        )

    def orderCollectiveAddElements(
        self, request: OrderCollectiveAddElementsRequest
    ) -> OrderCollectiveAddElementsResponse:
        return self._invoke(
            method="orderCollectiveAddElements",
            request=request,
            response_cls=OrderCollectiveAddElementsResponse,
            skip_block=False,
            req_mapping={},
            resp_mapping={},
        )

    def orderSetPaid(self, request: OrderSetPaidRequest) -> OrderSetPaidResponse:
        return self._invoke(
            method="orderSetPaid",
            request=request,
            response_cls=OrderSetPaidResponse,
            skip_block=False,
            req_mapping={},
            resp_mapping={},
        )

    def orderCheckPaid(self, request: OrderCheckPaidRequest) -> OrderCheckPaidResponse:
        return self._invoke(
            method="orderCheckPaid",
            request=request,
            response_cls=OrderCheckPaidResponse,
            skip_block=False,
            req_mapping={},
            resp_mapping={},
        )

    def orderPaidChangeList(
        self, request: OrderPaidChangeListRequest
    ) -> OrderPaidChangeListResponse:
        return self._invoke(
            method="orderPaidChangeList",
            request=request,
            response_cls=OrderPaidChangeListResponse,
            skip_block=False,
            req_mapping={},
            resp_mapping={},
        )

    def invoiceAdd(self, request: InvoiceAddRequest) -> InvoiceAddResponse:
        return self._invoke(
            method="invoiceAdd",
            request=request,
            response_cls=InvoiceAddResponse,
            skip_block=False,
            req_mapping={},
            resp_mapping={},
        )

    def invoiceAddPrepayment(
        self, request: InvoiceAddPrepaymentRequest
    ) -> InvoiceAddPrepaymentResponse:
        return self._invoke(
            method="invoiceAddPrepayment",
            request=request,
            response_cls=InvoiceAddPrepaymentResponse,
            skip_block=False,
            req_mapping={},
            resp_mapping={},
        )

    def invoiceAddFinal(
        self, request: InvoiceAddFinalRequest
    ) -> InvoiceAddFinalResponse:
        return self._invoke(
            method="invoiceAddFinal",
            request=request,
            response_cls=InvoiceAddFinalResponse,
            skip_block=False,
            req_mapping={},
            resp_mapping={},
        )

    def invoiceDetails(self, request: InvoiceDetailsRequest) -> InvoiceDetailsResponse:
        return self._invoke(
            method="invoiceDetails",
            request=request,
            response_cls=InvoiceDetailsResponse,
            skip_block=False,
            req_mapping={},
            resp_mapping={},
        )

    def invoiceDownload(
        self, request: InvoiceDownloadRequest
    ) -> InvoiceDownloadResponse:
        return self._invoke(
            method="invoiceDownload",
            request=request,
            response_cls=InvoiceDownloadResponse,
            skip_block=False,
            req_mapping={},
            resp_mapping={},
        )

    def invoiceStorno(self, request: InvoiceStornoRequest) -> InvoiceStornoResponse:
        return self._invoke(
            method="invoiceStorno",
            request=request,
            response_cls=InvoiceStornoResponse,
            skip_block=False,
            req_mapping={},
            resp_mapping={},
        )

    def invoiceList(self, request: InvoiceListRequest) -> InvoiceListResponse:
        return self._invoke(
            method="invoiceList",
            request=request,
            response_cls=InvoiceListResponse,
            skip_block=False,
            req_mapping={"from_": "from"},
            resp_mapping={},
        )

    def invoiceExport(self, request: InvoiceExportRequest) -> InvoiceExportResponse:
        return self._invoke(
            method="invoiceExport",
            request=request,
            response_cls=InvoiceExportResponse,
            skip_block=False,
            req_mapping={},
            resp_mapping={},
        )

    def invoiceSearch(self, request: InvoiceSearchRequest) -> InvoiceSearchResponse:
        return self._invoke(
            method="invoiceSearch",
            request=request,
            response_cls=InvoiceSearchResponse,
            skip_block=False,
            req_mapping={},
            resp_mapping={},
        )

    def invoiceCorrection(
        self, request: InvoiceCorrectionRequest
    ) -> InvoiceCorrectionResponse:
        return self._invoke(
            method="invoiceCorrection",
            request=request,
            response_cls=InvoiceCorrectionResponse,
            skip_block=True,
            req_mapping={},
            resp_mapping={},
        )

    def invoiceResend(self, request: InvoiceResendRequest) -> InvoiceResendResponse:
        return self._invoke(
            method="invoiceResend",
            request=request,
            response_cls=InvoiceResendResponse,
            skip_block=False,
            req_mapping={},
            resp_mapping={},
        )

    def invoiceCheckPaid(
        self, request: InvoiceCheckPaidRequest
    ) -> InvoiceCheckPaidResponse:
        return self._invoke(
            method="invoiceCheckPaid",
            request=request,
            response_cls=InvoiceCheckPaidResponse,
            skip_block=False,
            req_mapping={},
            resp_mapping={},
        )

    def invoiceSetPaid(self, request: InvoiceSetPaidRequest) -> InvoiceSetPaidResponse:
        return self._invoke(
            method="invoiceSetPaid",
            request=request,
            response_cls=InvoiceSetPaidResponse,
            skip_block=False,
            req_mapping={},
            resp_mapping={},
        )

    def debtDetails(self, request: DebtDetailsRequest) -> DebtDetailsResponse:
        return self._invoke(
            method="debtDetails",
            request=request,
            response_cls=DebtDetailsResponse,
            skip_block=True,
            req_mapping={},
            resp_mapping={},
        )

    def debtDownload(self, request: DebtDownloadRequest) -> DebtDownloadResponse:
        return self._invoke(
            method="debtDownload",
            request=request,
            response_cls=DebtDownloadResponse,
            skip_block=True,
            req_mapping={},
            resp_mapping={},
        )

    def debtList(self, request: DebtListRequest) -> DebtListResponse:
        return self._invoke(
            method="debtList",
            request=request,
            response_cls=DebtListResponse,
            skip_block=True,
            req_mapping={"from_": "from"},
            resp_mapping={},
        )

    def debtAdd(self, request: DebtAddRequest) -> DebtAddResponse:
        return self._invoke(
            method="debtAdd",
            request=request,
            response_cls=DebtAddResponse,
            skip_block=True,
            req_mapping={},
            resp_mapping={},
        )

    def debtModify(self, request: DebtModifyRequest) -> DebtModifyResponse:
        return self._invoke(
            method="debtModify",
            request=request,
            response_cls=DebtModifyResponse,
            skip_block=True,
            req_mapping={},
            resp_mapping={},
        )

    def debtAccept(self, request: DebtAcceptRequest) -> DebtAcceptResponse:
        return self._invoke(
            method="debtAccept",
            request=request,
            response_cls=DebtAcceptResponse,
            skip_block=True,
            req_mapping={},
            resp_mapping={},
        )

    def debtPay(self, request: DebtPayRequest) -> DebtPayResponse:
        return self._invoke(
            method="debtPay",
            request=request,
            response_cls=DebtPayResponse,
            skip_block=True,
            req_mapping={},
            resp_mapping={},
        )

    def debtDelete(self, request: DebtDeleteRequest) -> DebtDeleteResponse:
        return self._invoke(
            method="debtDelete",
            request=request,
            response_cls=DebtDeleteResponse,
            skip_block=True,
            req_mapping={},
            resp_mapping={},
        )

    def debtGenerate(self, request: DebtGenerateRequest) -> DebtGenerateResponse:
        return self._invoke(
            method="debtGenerate",
            request=request,
            response_cls=DebtGenerateResponse,
            skip_block=True,
            req_mapping={},
            resp_mapping={},
        )

    def debtExport(self, request: DebtExportRequest) -> DebtExportResponse:
        return self._invoke(
            method="debtExport",
            request=request,
            response_cls=DebtExportResponse,
            skip_block=True,
            req_mapping={},
            resp_mapping={},
        )

    def systemMessageList(
        self, request: SystemMessageListRequest
    ) -> SystemMessageListResponse:
        return self._invoke(
            method="systemMessageList",
            request=request,
            response_cls=SystemMessageListResponse,
            skip_block=True,
            req_mapping={},
            resp_mapping={},
        )

    def systemMessageSetRead(
        self, request: SystemMessageSetReadRequest
    ) -> SystemMessageSetReadResponse:
        return self._invoke(
            method="systemMessageSetRead",
            request=request,
            response_cls=SystemMessageSetReadResponse,
            skip_block=True,
            req_mapping={},
            resp_mapping={},
        )

    def systemErrorCodeList(
        self, request: SystemErrorCodeListRequest
    ) -> SystemErrorCodeListResponse:
        return self._invoke(
            method="systemErrorCodeList",
            request=request,
            response_cls=SystemErrorCodeListResponse,
            skip_block=True,
            req_mapping={},
            resp_mapping={},
        )

    def getVersion(self, request: GetVersionRequest) -> GetVersionResponse:
        return self._invoke(
            method="getVersion",
            request=request,
            response_cls=GetVersionResponse,
            skip_block=True,
            req_mapping={},
            resp_mapping={},
        )

    def serviceProviderDatas(
        self, request: ServiceProviderDatasRequest
    ) -> ServiceProviderDatasResponse:
        return self._invoke(
            method="serviceProviderDatas",
            request=request,
            response_cls=ServiceProviderDatasResponse,
            skip_block=True,
            req_mapping={},
            resp_mapping={},
        )

    def companyData(self, request: CompanyDataRequest) -> CompanyDataResponse:
        return self._invoke(
            method="companyData",
            request=request,
            response_cls=CompanyDataResponse,
            skip_block=True,
            req_mapping={},
            resp_mapping={},
        )

    def quantityList(self, request: QuantityListRequest) -> QuantityListResponse:
        return self._invoke(
            method="quantityList",
            request=request,
            response_cls=QuantityListResponse,
            skip_block=True,
            req_mapping={},
            resp_mapping={},
        )

    def currencyDownload(
        self, request: CurrencyDownloadRequest
    ) -> CurrencyDownloadResponse:
        return self._invoke(
            method="currencyDownload",
            request=request,
            response_cls=CurrencyDownloadResponse,
            skip_block=True,
            req_mapping={},
            resp_mapping={},
        )

    def regularityDownload(
        self, request: RegularityDownloadRequest
    ) -> RegularityDownloadResponse:
        return self._invoke(
            method="regularityDownload",
            request=request,
            response_cls=RegularityDownloadResponse,
            skip_block=True,
            req_mapping={},
            resp_mapping={},
        )

    def countryDownload(
        self, request: CountryDownloadRequest
    ) -> CountryDownloadResponse:
        return self._invoke(
            method="countryDownload",
            request=request,
            response_cls=CountryDownloadResponse,
            skip_block=True,
            req_mapping={},
            resp_mapping={},
        )

    def postcodeDownload(
        self, request: PostcodeDownloadRequest
    ) -> PostcodeDownloadResponse:
        return self._invoke(
            method="postcodeDownload",
            request=request,
            response_cls=PostcodeDownloadResponse,
            skip_block=True,
            req_mapping={},
            resp_mapping={},
        )

    def ping(self, request: PingRequest) -> PingResponse:
        return self._invoke(
            method="ping",
            request=request,
            response_cls=PingResponse,
            skip_block=True,
            req_mapping={},
            resp_mapping={},
        )

    def monitor(self, request: MonitorRequest) -> MonitorResponse:
        return self._invoke(
            method="monitor",
            request=request,
            response_cls=MonitorResponse,
            skip_block=True,
            req_mapping={},
            resp_mapping={},
        )
