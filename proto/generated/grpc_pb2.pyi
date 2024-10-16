import pb_pb2 as _pb_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RegisterDisputeAgentRequest(_message.Message):
    __slots__ = ("dispute_agent_type", "registration_key")
    DISPUTE_AGENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    REGISTRATION_KEY_FIELD_NUMBER: _ClassVar[int]
    dispute_agent_type: str
    registration_key: str
    def __init__(self, dispute_agent_type: _Optional[str] = ..., registration_key: _Optional[str] = ...) -> None: ...

class RegisterDisputeAgentReply(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetMethodHelpRequest(_message.Message):
    __slots__ = ("method_name",)
    METHOD_NAME_FIELD_NUMBER: _ClassVar[int]
    method_name: str
    def __init__(self, method_name: _Optional[str] = ...) -> None: ...

class GetMethodHelpReply(_message.Message):
    __slots__ = ("method_help",)
    METHOD_HELP_FIELD_NUMBER: _ClassVar[int]
    method_help: str
    def __init__(self, method_help: _Optional[str] = ...) -> None: ...

class GetOfferCategoryRequest(_message.Message):
    __slots__ = ("id", "is_my_offer")
    ID_FIELD_NUMBER: _ClassVar[int]
    IS_MY_OFFER_FIELD_NUMBER: _ClassVar[int]
    id: str
    is_my_offer: bool
    def __init__(self, id: _Optional[str] = ..., is_my_offer: bool = ...) -> None: ...

class GetOfferCategoryReply(_message.Message):
    __slots__ = ("offer_category",)
    class OfferCategory(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[GetOfferCategoryReply.OfferCategory]
        FIAT: _ClassVar[GetOfferCategoryReply.OfferCategory]
        ALTCOIN: _ClassVar[GetOfferCategoryReply.OfferCategory]
        BSQ_SWAP: _ClassVar[GetOfferCategoryReply.OfferCategory]
    UNKNOWN: GetOfferCategoryReply.OfferCategory
    FIAT: GetOfferCategoryReply.OfferCategory
    ALTCOIN: GetOfferCategoryReply.OfferCategory
    BSQ_SWAP: GetOfferCategoryReply.OfferCategory
    OFFER_CATEGORY_FIELD_NUMBER: _ClassVar[int]
    offer_category: GetOfferCategoryReply.OfferCategory
    def __init__(self, offer_category: _Optional[_Union[GetOfferCategoryReply.OfferCategory, str]] = ...) -> None: ...

class GetBsqSwapOfferReply(_message.Message):
    __slots__ = ("bsq_swap_offer",)
    BSQ_SWAP_OFFER_FIELD_NUMBER: _ClassVar[int]
    bsq_swap_offer: OfferInfo
    def __init__(self, bsq_swap_offer: _Optional[_Union[OfferInfo, _Mapping]] = ...) -> None: ...

class GetOfferRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetOfferReply(_message.Message):
    __slots__ = ("offer",)
    OFFER_FIELD_NUMBER: _ClassVar[int]
    offer: OfferInfo
    def __init__(self, offer: _Optional[_Union[OfferInfo, _Mapping]] = ...) -> None: ...

class GetMyBsqSwapOfferReply(_message.Message):
    __slots__ = ("bsq_swap_offer",)
    BSQ_SWAP_OFFER_FIELD_NUMBER: _ClassVar[int]
    bsq_swap_offer: OfferInfo
    def __init__(self, bsq_swap_offer: _Optional[_Union[OfferInfo, _Mapping]] = ...) -> None: ...

class GetMyOfferRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetMyOfferReply(_message.Message):
    __slots__ = ("offer",)
    OFFER_FIELD_NUMBER: _ClassVar[int]
    offer: OfferInfo
    def __init__(self, offer: _Optional[_Union[OfferInfo, _Mapping]] = ...) -> None: ...

class GetOffersRequest(_message.Message):
    __slots__ = ("direction", "currency_code", "all")
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_CODE_FIELD_NUMBER: _ClassVar[int]
    ALL_FIELD_NUMBER: _ClassVar[int]
    direction: str
    currency_code: str
    all: bool
    def __init__(self, direction: _Optional[str] = ..., currency_code: _Optional[str] = ..., all: bool = ...) -> None: ...

class GetOffersReply(_message.Message):
    __slots__ = ("offers",)
    OFFERS_FIELD_NUMBER: _ClassVar[int]
    offers: _containers.RepeatedCompositeFieldContainer[OfferInfo]
    def __init__(self, offers: _Optional[_Iterable[_Union[OfferInfo, _Mapping]]] = ...) -> None: ...

class GetBsqSwapOffersRequest(_message.Message):
    __slots__ = ("direction",)
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    direction: str
    def __init__(self, direction: _Optional[str] = ...) -> None: ...

class GetBsqSwapOffersReply(_message.Message):
    __slots__ = ("bsq_swap_offers",)
    BSQ_SWAP_OFFERS_FIELD_NUMBER: _ClassVar[int]
    bsq_swap_offers: _containers.RepeatedCompositeFieldContainer[OfferInfo]
    def __init__(self, bsq_swap_offers: _Optional[_Iterable[_Union[OfferInfo, _Mapping]]] = ...) -> None: ...

class GetMyOffersRequest(_message.Message):
    __slots__ = ("direction", "currency_code")
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_CODE_FIELD_NUMBER: _ClassVar[int]
    direction: str
    currency_code: str
    def __init__(self, direction: _Optional[str] = ..., currency_code: _Optional[str] = ...) -> None: ...

class GetMyOffersReply(_message.Message):
    __slots__ = ("offers",)
    OFFERS_FIELD_NUMBER: _ClassVar[int]
    offers: _containers.RepeatedCompositeFieldContainer[OfferInfo]
    def __init__(self, offers: _Optional[_Iterable[_Union[OfferInfo, _Mapping]]] = ...) -> None: ...

class GetMyBsqSwapOffersReply(_message.Message):
    __slots__ = ("bsq_swap_offers",)
    BSQ_SWAP_OFFERS_FIELD_NUMBER: _ClassVar[int]
    bsq_swap_offers: _containers.RepeatedCompositeFieldContainer[OfferInfo]
    def __init__(self, bsq_swap_offers: _Optional[_Iterable[_Union[OfferInfo, _Mapping]]] = ...) -> None: ...

class CreateBsqSwapOfferRequest(_message.Message):
    __slots__ = ("direction", "amount", "min_amount", "price")
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    MIN_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    direction: str
    amount: int
    min_amount: int
    price: str
    def __init__(self, direction: _Optional[str] = ..., amount: _Optional[int] = ..., min_amount: _Optional[int] = ..., price: _Optional[str] = ...) -> None: ...

class CreateBsqSwapOfferReply(_message.Message):
    __slots__ = ("bsq_swap_offer",)
    BSQ_SWAP_OFFER_FIELD_NUMBER: _ClassVar[int]
    bsq_swap_offer: OfferInfo
    def __init__(self, bsq_swap_offer: _Optional[_Union[OfferInfo, _Mapping]] = ...) -> None: ...

class CreateOfferRequest(_message.Message):
    __slots__ = ("currency_code", "direction", "price", "use_market_based_price", "market_price_margin_pct", "amount", "min_amount", "buyer_security_deposit_pct", "trigger_price", "payment_account_id", "maker_fee_currency_code")
    CURRENCY_CODE_FIELD_NUMBER: _ClassVar[int]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    USE_MARKET_BASED_PRICE_FIELD_NUMBER: _ClassVar[int]
    MARKET_PRICE_MARGIN_PCT_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    MIN_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    BUYER_SECURITY_DEPOSIT_PCT_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_PRICE_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    MAKER_FEE_CURRENCY_CODE_FIELD_NUMBER: _ClassVar[int]
    currency_code: str
    direction: str
    price: str
    use_market_based_price: bool
    market_price_margin_pct: float
    amount: int
    min_amount: int
    buyer_security_deposit_pct: float
    trigger_price: str
    payment_account_id: str
    maker_fee_currency_code: str
    def __init__(self, currency_code: _Optional[str] = ..., direction: _Optional[str] = ..., price: _Optional[str] = ..., use_market_based_price: bool = ..., market_price_margin_pct: _Optional[float] = ..., amount: _Optional[int] = ..., min_amount: _Optional[int] = ..., buyer_security_deposit_pct: _Optional[float] = ..., trigger_price: _Optional[str] = ..., payment_account_id: _Optional[str] = ..., maker_fee_currency_code: _Optional[str] = ...) -> None: ...

class CreateOfferReply(_message.Message):
    __slots__ = ("offer",)
    OFFER_FIELD_NUMBER: _ClassVar[int]
    offer: OfferInfo
    def __init__(self, offer: _Optional[_Union[OfferInfo, _Mapping]] = ...) -> None: ...

class EditOfferRequest(_message.Message):
    __slots__ = ("id", "price", "use_market_based_price", "market_price_margin_pct", "trigger_price", "enable", "edit_type")
    class EditType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ACTIVATION_STATE_ONLY: _ClassVar[EditOfferRequest.EditType]
        FIXED_PRICE_ONLY: _ClassVar[EditOfferRequest.EditType]
        FIXED_PRICE_AND_ACTIVATION_STATE: _ClassVar[EditOfferRequest.EditType]
        MKT_PRICE_MARGIN_ONLY: _ClassVar[EditOfferRequest.EditType]
        MKT_PRICE_MARGIN_AND_ACTIVATION_STATE: _ClassVar[EditOfferRequest.EditType]
        TRIGGER_PRICE_ONLY: _ClassVar[EditOfferRequest.EditType]
        TRIGGER_PRICE_AND_ACTIVATION_STATE: _ClassVar[EditOfferRequest.EditType]
        MKT_PRICE_MARGIN_AND_TRIGGER_PRICE: _ClassVar[EditOfferRequest.EditType]
        MKT_PRICE_MARGIN_AND_TRIGGER_PRICE_AND_ACTIVATION_STATE: _ClassVar[EditOfferRequest.EditType]
    ACTIVATION_STATE_ONLY: EditOfferRequest.EditType
    FIXED_PRICE_ONLY: EditOfferRequest.EditType
    FIXED_PRICE_AND_ACTIVATION_STATE: EditOfferRequest.EditType
    MKT_PRICE_MARGIN_ONLY: EditOfferRequest.EditType
    MKT_PRICE_MARGIN_AND_ACTIVATION_STATE: EditOfferRequest.EditType
    TRIGGER_PRICE_ONLY: EditOfferRequest.EditType
    TRIGGER_PRICE_AND_ACTIVATION_STATE: EditOfferRequest.EditType
    MKT_PRICE_MARGIN_AND_TRIGGER_PRICE: EditOfferRequest.EditType
    MKT_PRICE_MARGIN_AND_TRIGGER_PRICE_AND_ACTIVATION_STATE: EditOfferRequest.EditType
    ID_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    USE_MARKET_BASED_PRICE_FIELD_NUMBER: _ClassVar[int]
    MARKET_PRICE_MARGIN_PCT_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_PRICE_FIELD_NUMBER: _ClassVar[int]
    ENABLE_FIELD_NUMBER: _ClassVar[int]
    EDIT_TYPE_FIELD_NUMBER: _ClassVar[int]
    id: str
    price: str
    use_market_based_price: bool
    market_price_margin_pct: float
    trigger_price: str
    enable: int
    edit_type: EditOfferRequest.EditType
    def __init__(self, id: _Optional[str] = ..., price: _Optional[str] = ..., use_market_based_price: bool = ..., market_price_margin_pct: _Optional[float] = ..., trigger_price: _Optional[str] = ..., enable: _Optional[int] = ..., edit_type: _Optional[_Union[EditOfferRequest.EditType, str]] = ...) -> None: ...

class EditOfferReply(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CancelOfferRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class CancelOfferReply(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class OfferInfo(_message.Message):
    __slots__ = ("id", "direction", "price", "use_market_based_price", "market_price_margin_pct", "amount", "min_amount", "volume", "min_volume", "buyer_security_deposit", "trigger_price", "is_currency_for_maker_fee_btc", "payment_account_id", "payment_method_id", "payment_method_short_name", "base_currency_code", "counter_currency_code", "date", "state", "seller_security_deposit", "offer_fee_payment_tx_id", "tx_fee", "maker_fee", "is_activated", "is_my_offer", "is_my_pending_offer", "is_bsq_swap_offer", "owner_node_address", "pub_key_ring", "version_nr", "protocol_version")
    ID_FIELD_NUMBER: _ClassVar[int]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    USE_MARKET_BASED_PRICE_FIELD_NUMBER: _ClassVar[int]
    MARKET_PRICE_MARGIN_PCT_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    MIN_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    VOLUME_FIELD_NUMBER: _ClassVar[int]
    MIN_VOLUME_FIELD_NUMBER: _ClassVar[int]
    BUYER_SECURITY_DEPOSIT_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_PRICE_FIELD_NUMBER: _ClassVar[int]
    IS_CURRENCY_FOR_MAKER_FEE_BTC_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_METHOD_ID_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_METHOD_SHORT_NAME_FIELD_NUMBER: _ClassVar[int]
    BASE_CURRENCY_CODE_FIELD_NUMBER: _ClassVar[int]
    COUNTER_CURRENCY_CODE_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    SELLER_SECURITY_DEPOSIT_FIELD_NUMBER: _ClassVar[int]
    OFFER_FEE_PAYMENT_TX_ID_FIELD_NUMBER: _ClassVar[int]
    TX_FEE_FIELD_NUMBER: _ClassVar[int]
    MAKER_FEE_FIELD_NUMBER: _ClassVar[int]
    IS_ACTIVATED_FIELD_NUMBER: _ClassVar[int]
    IS_MY_OFFER_FIELD_NUMBER: _ClassVar[int]
    IS_MY_PENDING_OFFER_FIELD_NUMBER: _ClassVar[int]
    IS_BSQ_SWAP_OFFER_FIELD_NUMBER: _ClassVar[int]
    OWNER_NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PUB_KEY_RING_FIELD_NUMBER: _ClassVar[int]
    VERSION_NR_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_VERSION_FIELD_NUMBER: _ClassVar[int]
    id: str
    direction: str
    price: str
    use_market_based_price: bool
    market_price_margin_pct: float
    amount: int
    min_amount: int
    volume: str
    min_volume: str
    buyer_security_deposit: int
    trigger_price: str
    is_currency_for_maker_fee_btc: bool
    payment_account_id: str
    payment_method_id: str
    payment_method_short_name: str
    base_currency_code: str
    counter_currency_code: str
    date: int
    state: str
    seller_security_deposit: int
    offer_fee_payment_tx_id: str
    tx_fee: int
    maker_fee: int
    is_activated: bool
    is_my_offer: bool
    is_my_pending_offer: bool
    is_bsq_swap_offer: bool
    owner_node_address: str
    pub_key_ring: str
    version_nr: str
    protocol_version: int
    def __init__(self, id: _Optional[str] = ..., direction: _Optional[str] = ..., price: _Optional[str] = ..., use_market_based_price: bool = ..., market_price_margin_pct: _Optional[float] = ..., amount: _Optional[int] = ..., min_amount: _Optional[int] = ..., volume: _Optional[str] = ..., min_volume: _Optional[str] = ..., buyer_security_deposit: _Optional[int] = ..., trigger_price: _Optional[str] = ..., is_currency_for_maker_fee_btc: bool = ..., payment_account_id: _Optional[str] = ..., payment_method_id: _Optional[str] = ..., payment_method_short_name: _Optional[str] = ..., base_currency_code: _Optional[str] = ..., counter_currency_code: _Optional[str] = ..., date: _Optional[int] = ..., state: _Optional[str] = ..., seller_security_deposit: _Optional[int] = ..., offer_fee_payment_tx_id: _Optional[str] = ..., tx_fee: _Optional[int] = ..., maker_fee: _Optional[int] = ..., is_activated: bool = ..., is_my_offer: bool = ..., is_my_pending_offer: bool = ..., is_bsq_swap_offer: bool = ..., owner_node_address: _Optional[str] = ..., pub_key_ring: _Optional[str] = ..., version_nr: _Optional[str] = ..., protocol_version: _Optional[int] = ...) -> None: ...

class AvailabilityResultWithDescription(_message.Message):
    __slots__ = ("availability_result", "description")
    AVAILABILITY_RESULT_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    availability_result: _pb_pb2.AvailabilityResult
    description: str
    def __init__(self, availability_result: _Optional[_Union[_pb_pb2.AvailabilityResult, str]] = ..., description: _Optional[str] = ...) -> None: ...

class CreatePaymentAccountRequest(_message.Message):
    __slots__ = ("payment_account_form",)
    PAYMENT_ACCOUNT_FORM_FIELD_NUMBER: _ClassVar[int]
    payment_account_form: str
    def __init__(self, payment_account_form: _Optional[str] = ...) -> None: ...

class CreatePaymentAccountReply(_message.Message):
    __slots__ = ("payment_account",)
    PAYMENT_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    payment_account: _pb_pb2.PaymentAccount
    def __init__(self, payment_account: _Optional[_Union[_pb_pb2.PaymentAccount, _Mapping]] = ...) -> None: ...

class GetPaymentAccountsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetPaymentAccountsReply(_message.Message):
    __slots__ = ("payment_accounts",)
    PAYMENT_ACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    payment_accounts: _containers.RepeatedCompositeFieldContainer[_pb_pb2.PaymentAccount]
    def __init__(self, payment_accounts: _Optional[_Iterable[_Union[_pb_pb2.PaymentAccount, _Mapping]]] = ...) -> None: ...

class GetPaymentMethodsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetPaymentMethodsReply(_message.Message):
    __slots__ = ("payment_methods",)
    PAYMENT_METHODS_FIELD_NUMBER: _ClassVar[int]
    payment_methods: _containers.RepeatedCompositeFieldContainer[_pb_pb2.PaymentMethod]
    def __init__(self, payment_methods: _Optional[_Iterable[_Union[_pb_pb2.PaymentMethod, _Mapping]]] = ...) -> None: ...

class GetPaymentAccountFormRequest(_message.Message):
    __slots__ = ("payment_method_id",)
    PAYMENT_METHOD_ID_FIELD_NUMBER: _ClassVar[int]
    payment_method_id: str
    def __init__(self, payment_method_id: _Optional[str] = ...) -> None: ...

class GetPaymentAccountFormReply(_message.Message):
    __slots__ = ("payment_account_form_json",)
    PAYMENT_ACCOUNT_FORM_JSON_FIELD_NUMBER: _ClassVar[int]
    payment_account_form_json: str
    def __init__(self, payment_account_form_json: _Optional[str] = ...) -> None: ...

class CreateCryptoCurrencyPaymentAccountRequest(_message.Message):
    __slots__ = ("account_name", "currency_code", "address", "trade_instant")
    ACCOUNT_NAME_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_CODE_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    TRADE_INSTANT_FIELD_NUMBER: _ClassVar[int]
    account_name: str
    currency_code: str
    address: str
    trade_instant: bool
    def __init__(self, account_name: _Optional[str] = ..., currency_code: _Optional[str] = ..., address: _Optional[str] = ..., trade_instant: bool = ...) -> None: ...

class CreateCryptoCurrencyPaymentAccountReply(_message.Message):
    __slots__ = ("payment_account",)
    PAYMENT_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    payment_account: _pb_pb2.PaymentAccount
    def __init__(self, payment_account: _Optional[_Union[_pb_pb2.PaymentAccount, _Mapping]] = ...) -> None: ...

class GetCryptoCurrencyPaymentMethodsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetCryptoCurrencyPaymentMethodsReply(_message.Message):
    __slots__ = ("payment_methods",)
    PAYMENT_METHODS_FIELD_NUMBER: _ClassVar[int]
    payment_methods: _containers.RepeatedCompositeFieldContainer[_pb_pb2.PaymentMethod]
    def __init__(self, payment_methods: _Optional[_Iterable[_Union[_pb_pb2.PaymentMethod, _Mapping]]] = ...) -> None: ...

class MarketPriceRequest(_message.Message):
    __slots__ = ("currency_code",)
    CURRENCY_CODE_FIELD_NUMBER: _ClassVar[int]
    currency_code: str
    def __init__(self, currency_code: _Optional[str] = ...) -> None: ...

class MarketPriceReply(_message.Message):
    __slots__ = ("price",)
    PRICE_FIELD_NUMBER: _ClassVar[int]
    price: float
    def __init__(self, price: _Optional[float] = ...) -> None: ...

class GetAverageBsqTradePriceRequest(_message.Message):
    __slots__ = ("days",)
    DAYS_FIELD_NUMBER: _ClassVar[int]
    days: int
    def __init__(self, days: _Optional[int] = ...) -> None: ...

class GetAverageBsqTradePriceReply(_message.Message):
    __slots__ = ("price",)
    PRICE_FIELD_NUMBER: _ClassVar[int]
    price: AverageBsqTradePrice
    def __init__(self, price: _Optional[_Union[AverageBsqTradePrice, _Mapping]] = ...) -> None: ...

class AverageBsqTradePrice(_message.Message):
    __slots__ = ("usd_price", "btc_price")
    USD_PRICE_FIELD_NUMBER: _ClassVar[int]
    BTC_PRICE_FIELD_NUMBER: _ClassVar[int]
    usd_price: str
    btc_price: str
    def __init__(self, usd_price: _Optional[str] = ..., btc_price: _Optional[str] = ...) -> None: ...

class StopRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class StopReply(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TakeOfferRequest(_message.Message):
    __slots__ = ("offer_id", "payment_account_id", "taker_fee_currency_code", "amount")
    OFFER_ID_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    TAKER_FEE_CURRENCY_CODE_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    offer_id: str
    payment_account_id: str
    taker_fee_currency_code: str
    amount: int
    def __init__(self, offer_id: _Optional[str] = ..., payment_account_id: _Optional[str] = ..., taker_fee_currency_code: _Optional[str] = ..., amount: _Optional[int] = ...) -> None: ...

class TakeOfferReply(_message.Message):
    __slots__ = ("trade", "failure_reason")
    TRADE_FIELD_NUMBER: _ClassVar[int]
    FAILURE_REASON_FIELD_NUMBER: _ClassVar[int]
    trade: TradeInfo
    failure_reason: AvailabilityResultWithDescription
    def __init__(self, trade: _Optional[_Union[TradeInfo, _Mapping]] = ..., failure_reason: _Optional[_Union[AvailabilityResultWithDescription, _Mapping]] = ...) -> None: ...

class ConfirmPaymentStartedRequest(_message.Message):
    __slots__ = ("trade_id",)
    TRADE_ID_FIELD_NUMBER: _ClassVar[int]
    trade_id: str
    def __init__(self, trade_id: _Optional[str] = ...) -> None: ...

class ConfirmPaymentStartedXmrRequest(_message.Message):
    __slots__ = ("trade_id", "tx_id", "tx_key")
    TRADE_ID_FIELD_NUMBER: _ClassVar[int]
    TX_ID_FIELD_NUMBER: _ClassVar[int]
    TX_KEY_FIELD_NUMBER: _ClassVar[int]
    trade_id: str
    tx_id: str
    tx_key: str
    def __init__(self, trade_id: _Optional[str] = ..., tx_id: _Optional[str] = ..., tx_key: _Optional[str] = ...) -> None: ...

class ConfirmPaymentStartedReply(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ConfirmPaymentReceivedRequest(_message.Message):
    __slots__ = ("trade_id",)
    TRADE_ID_FIELD_NUMBER: _ClassVar[int]
    trade_id: str
    def __init__(self, trade_id: _Optional[str] = ...) -> None: ...

class ConfirmPaymentReceivedReply(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetTradeRequest(_message.Message):
    __slots__ = ("trade_id",)
    TRADE_ID_FIELD_NUMBER: _ClassVar[int]
    trade_id: str
    def __init__(self, trade_id: _Optional[str] = ...) -> None: ...

class GetTradeReply(_message.Message):
    __slots__ = ("trade",)
    TRADE_FIELD_NUMBER: _ClassVar[int]
    trade: TradeInfo
    def __init__(self, trade: _Optional[_Union[TradeInfo, _Mapping]] = ...) -> None: ...

class GetTradesRequest(_message.Message):
    __slots__ = ("category",)
    class Category(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OPEN: _ClassVar[GetTradesRequest.Category]
        CLOSED: _ClassVar[GetTradesRequest.Category]
        FAILED: _ClassVar[GetTradesRequest.Category]
    OPEN: GetTradesRequest.Category
    CLOSED: GetTradesRequest.Category
    FAILED: GetTradesRequest.Category
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    category: GetTradesRequest.Category
    def __init__(self, category: _Optional[_Union[GetTradesRequest.Category, str]] = ...) -> None: ...

class GetTradesReply(_message.Message):
    __slots__ = ("trades",)
    TRADES_FIELD_NUMBER: _ClassVar[int]
    trades: _containers.RepeatedCompositeFieldContainer[TradeInfo]
    def __init__(self, trades: _Optional[_Iterable[_Union[TradeInfo, _Mapping]]] = ...) -> None: ...

class CloseTradeRequest(_message.Message):
    __slots__ = ("trade_id",)
    TRADE_ID_FIELD_NUMBER: _ClassVar[int]
    trade_id: str
    def __init__(self, trade_id: _Optional[str] = ...) -> None: ...

class CloseTradeReply(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FailTradeRequest(_message.Message):
    __slots__ = ("trade_id",)
    TRADE_ID_FIELD_NUMBER: _ClassVar[int]
    trade_id: str
    def __init__(self, trade_id: _Optional[str] = ...) -> None: ...

class FailTradeReply(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UnFailTradeRequest(_message.Message):
    __slots__ = ("trade_id",)
    TRADE_ID_FIELD_NUMBER: _ClassVar[int]
    trade_id: str
    def __init__(self, trade_id: _Optional[str] = ...) -> None: ...

class UnFailTradeReply(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class WithdrawFundsRequest(_message.Message):
    __slots__ = ("trade_id", "address", "memo")
    TRADE_ID_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    MEMO_FIELD_NUMBER: _ClassVar[int]
    trade_id: str
    address: str
    memo: str
    def __init__(self, trade_id: _Optional[str] = ..., address: _Optional[str] = ..., memo: _Optional[str] = ...) -> None: ...

class WithdrawFundsReply(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TradeInfo(_message.Message):
    __slots__ = ("offer", "trade_id", "short_id", "date", "role", "is_currency_for_taker_fee_btc", "tx_fee_as_long", "taker_fee_as_long", "taker_fee_tx_id", "deposit_tx_id", "payout_tx_id", "trade_amount_as_long", "trade_price", "trading_peer_node_address", "state", "phase", "trade_period_state", "is_deposit_published", "is_deposit_confirmed", "is_payment_started_message_sent", "is_payment_received_message_sent", "is_payout_published", "is_completed", "contract_as_json", "contract", "trade_volume", "bsq_swap_trade_info", "closing_status", "has_failed", "error_message", "auto_conf_tx_id", "auto_conf_tx_key")
    OFFER_FIELD_NUMBER: _ClassVar[int]
    TRADE_ID_FIELD_NUMBER: _ClassVar[int]
    SHORT_ID_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    IS_CURRENCY_FOR_TAKER_FEE_BTC_FIELD_NUMBER: _ClassVar[int]
    TX_FEE_AS_LONG_FIELD_NUMBER: _ClassVar[int]
    TAKER_FEE_AS_LONG_FIELD_NUMBER: _ClassVar[int]
    TAKER_FEE_TX_ID_FIELD_NUMBER: _ClassVar[int]
    DEPOSIT_TX_ID_FIELD_NUMBER: _ClassVar[int]
    PAYOUT_TX_ID_FIELD_NUMBER: _ClassVar[int]
    TRADE_AMOUNT_AS_LONG_FIELD_NUMBER: _ClassVar[int]
    TRADE_PRICE_FIELD_NUMBER: _ClassVar[int]
    TRADING_PEER_NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    PHASE_FIELD_NUMBER: _ClassVar[int]
    TRADE_PERIOD_STATE_FIELD_NUMBER: _ClassVar[int]
    IS_DEPOSIT_PUBLISHED_FIELD_NUMBER: _ClassVar[int]
    IS_DEPOSIT_CONFIRMED_FIELD_NUMBER: _ClassVar[int]
    IS_PAYMENT_STARTED_MESSAGE_SENT_FIELD_NUMBER: _ClassVar[int]
    IS_PAYMENT_RECEIVED_MESSAGE_SENT_FIELD_NUMBER: _ClassVar[int]
    IS_PAYOUT_PUBLISHED_FIELD_NUMBER: _ClassVar[int]
    IS_COMPLETED_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_AS_JSON_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_FIELD_NUMBER: _ClassVar[int]
    TRADE_VOLUME_FIELD_NUMBER: _ClassVar[int]
    BSQ_SWAP_TRADE_INFO_FIELD_NUMBER: _ClassVar[int]
    CLOSING_STATUS_FIELD_NUMBER: _ClassVar[int]
    HAS_FAILED_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    AUTO_CONF_TX_ID_FIELD_NUMBER: _ClassVar[int]
    AUTO_CONF_TX_KEY_FIELD_NUMBER: _ClassVar[int]
    offer: OfferInfo
    trade_id: str
    short_id: str
    date: int
    role: str
    is_currency_for_taker_fee_btc: bool
    tx_fee_as_long: int
    taker_fee_as_long: int
    taker_fee_tx_id: str
    deposit_tx_id: str
    payout_tx_id: str
    trade_amount_as_long: int
    trade_price: str
    trading_peer_node_address: str
    state: str
    phase: str
    trade_period_state: str
    is_deposit_published: bool
    is_deposit_confirmed: bool
    is_payment_started_message_sent: bool
    is_payment_received_message_sent: bool
    is_payout_published: bool
    is_completed: bool
    contract_as_json: str
    contract: ContractInfo
    trade_volume: str
    bsq_swap_trade_info: BsqSwapTradeInfo
    closing_status: str
    has_failed: bool
    error_message: str
    auto_conf_tx_id: str
    auto_conf_tx_key: str
    def __init__(self, offer: _Optional[_Union[OfferInfo, _Mapping]] = ..., trade_id: _Optional[str] = ..., short_id: _Optional[str] = ..., date: _Optional[int] = ..., role: _Optional[str] = ..., is_currency_for_taker_fee_btc: bool = ..., tx_fee_as_long: _Optional[int] = ..., taker_fee_as_long: _Optional[int] = ..., taker_fee_tx_id: _Optional[str] = ..., deposit_tx_id: _Optional[str] = ..., payout_tx_id: _Optional[str] = ..., trade_amount_as_long: _Optional[int] = ..., trade_price: _Optional[str] = ..., trading_peer_node_address: _Optional[str] = ..., state: _Optional[str] = ..., phase: _Optional[str] = ..., trade_period_state: _Optional[str] = ..., is_deposit_published: bool = ..., is_deposit_confirmed: bool = ..., is_payment_started_message_sent: bool = ..., is_payment_received_message_sent: bool = ..., is_payout_published: bool = ..., is_completed: bool = ..., contract_as_json: _Optional[str] = ..., contract: _Optional[_Union[ContractInfo, _Mapping]] = ..., trade_volume: _Optional[str] = ..., bsq_swap_trade_info: _Optional[_Union[BsqSwapTradeInfo, _Mapping]] = ..., closing_status: _Optional[str] = ..., has_failed: bool = ..., error_message: _Optional[str] = ..., auto_conf_tx_id: _Optional[str] = ..., auto_conf_tx_key: _Optional[str] = ...) -> None: ...

class ContractInfo(_message.Message):
    __slots__ = ("buyer_node_address", "seller_node_address", "mediator_node_address", "refund_agent_node_address", "is_buyer_maker_and_seller_taker", "maker_account_id", "taker_account_id", "maker_payment_account_payload", "taker_payment_account_payload", "maker_payout_address_string", "taker_payout_address_string", "lock_time")
    BUYER_NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    SELLER_NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    MEDIATOR_NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    REFUND_AGENT_NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    IS_BUYER_MAKER_AND_SELLER_TAKER_FIELD_NUMBER: _ClassVar[int]
    MAKER_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    TAKER_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    MAKER_PAYMENT_ACCOUNT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    TAKER_PAYMENT_ACCOUNT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    MAKER_PAYOUT_ADDRESS_STRING_FIELD_NUMBER: _ClassVar[int]
    TAKER_PAYOUT_ADDRESS_STRING_FIELD_NUMBER: _ClassVar[int]
    LOCK_TIME_FIELD_NUMBER: _ClassVar[int]
    buyer_node_address: str
    seller_node_address: str
    mediator_node_address: str
    refund_agent_node_address: str
    is_buyer_maker_and_seller_taker: bool
    maker_account_id: str
    taker_account_id: str
    maker_payment_account_payload: PaymentAccountPayloadInfo
    taker_payment_account_payload: PaymentAccountPayloadInfo
    maker_payout_address_string: str
    taker_payout_address_string: str
    lock_time: int
    def __init__(self, buyer_node_address: _Optional[str] = ..., seller_node_address: _Optional[str] = ..., mediator_node_address: _Optional[str] = ..., refund_agent_node_address: _Optional[str] = ..., is_buyer_maker_and_seller_taker: bool = ..., maker_account_id: _Optional[str] = ..., taker_account_id: _Optional[str] = ..., maker_payment_account_payload: _Optional[_Union[PaymentAccountPayloadInfo, _Mapping]] = ..., taker_payment_account_payload: _Optional[_Union[PaymentAccountPayloadInfo, _Mapping]] = ..., maker_payout_address_string: _Optional[str] = ..., taker_payout_address_string: _Optional[str] = ..., lock_time: _Optional[int] = ...) -> None: ...

class BsqSwapTradeInfo(_message.Message):
    __slots__ = ("tx_id", "bsq_trade_amount", "btc_trade_amount", "bsq_maker_trade_fee", "bsq_taker_trade_fee", "tx_fee_per_vbyte", "maker_bsq_address", "maker_btc_address", "taker_bsq_address", "taker_btc_address", "num_confirmations", "error_message", "payout", "swap_peer_payout")
    TX_ID_FIELD_NUMBER: _ClassVar[int]
    BSQ_TRADE_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    BTC_TRADE_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    BSQ_MAKER_TRADE_FEE_FIELD_NUMBER: _ClassVar[int]
    BSQ_TAKER_TRADE_FEE_FIELD_NUMBER: _ClassVar[int]
    TX_FEE_PER_VBYTE_FIELD_NUMBER: _ClassVar[int]
    MAKER_BSQ_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    MAKER_BTC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    TAKER_BSQ_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    TAKER_BTC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    NUM_CONFIRMATIONS_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    PAYOUT_FIELD_NUMBER: _ClassVar[int]
    SWAP_PEER_PAYOUT_FIELD_NUMBER: _ClassVar[int]
    tx_id: str
    bsq_trade_amount: int
    btc_trade_amount: int
    bsq_maker_trade_fee: int
    bsq_taker_trade_fee: int
    tx_fee_per_vbyte: int
    maker_bsq_address: str
    maker_btc_address: str
    taker_bsq_address: str
    taker_btc_address: str
    num_confirmations: int
    error_message: str
    payout: int
    swap_peer_payout: int
    def __init__(self, tx_id: _Optional[str] = ..., bsq_trade_amount: _Optional[int] = ..., btc_trade_amount: _Optional[int] = ..., bsq_maker_trade_fee: _Optional[int] = ..., bsq_taker_trade_fee: _Optional[int] = ..., tx_fee_per_vbyte: _Optional[int] = ..., maker_bsq_address: _Optional[str] = ..., maker_btc_address: _Optional[str] = ..., taker_bsq_address: _Optional[str] = ..., taker_btc_address: _Optional[str] = ..., num_confirmations: _Optional[int] = ..., error_message: _Optional[str] = ..., payout: _Optional[int] = ..., swap_peer_payout: _Optional[int] = ...) -> None: ...

class PaymentAccountPayloadInfo(_message.Message):
    __slots__ = ("id", "payment_method_id", "address", "payment_details")
    ID_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_METHOD_ID_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_DETAILS_FIELD_NUMBER: _ClassVar[int]
    id: str
    payment_method_id: str
    address: str
    payment_details: str
    def __init__(self, id: _Optional[str] = ..., payment_method_id: _Optional[str] = ..., address: _Optional[str] = ..., payment_details: _Optional[str] = ...) -> None: ...

class TxFeeRateInfo(_message.Message):
    __slots__ = ("use_custom_tx_fee_rate", "custom_tx_fee_rate", "fee_service_rate", "last_fee_service_request_ts", "min_fee_service_rate")
    USE_CUSTOM_TX_FEE_RATE_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_TX_FEE_RATE_FIELD_NUMBER: _ClassVar[int]
    FEE_SERVICE_RATE_FIELD_NUMBER: _ClassVar[int]
    LAST_FEE_SERVICE_REQUEST_TS_FIELD_NUMBER: _ClassVar[int]
    MIN_FEE_SERVICE_RATE_FIELD_NUMBER: _ClassVar[int]
    use_custom_tx_fee_rate: bool
    custom_tx_fee_rate: int
    fee_service_rate: int
    last_fee_service_request_ts: int
    min_fee_service_rate: int
    def __init__(self, use_custom_tx_fee_rate: bool = ..., custom_tx_fee_rate: _Optional[int] = ..., fee_service_rate: _Optional[int] = ..., last_fee_service_request_ts: _Optional[int] = ..., min_fee_service_rate: _Optional[int] = ...) -> None: ...

class TxInfo(_message.Message):
    __slots__ = ("tx_id", "input_sum", "output_sum", "fee", "size", "is_pending", "memo")
    TX_ID_FIELD_NUMBER: _ClassVar[int]
    INPUT_SUM_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_SUM_FIELD_NUMBER: _ClassVar[int]
    FEE_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    IS_PENDING_FIELD_NUMBER: _ClassVar[int]
    MEMO_FIELD_NUMBER: _ClassVar[int]
    tx_id: str
    input_sum: int
    output_sum: int
    fee: int
    size: int
    is_pending: bool
    memo: str
    def __init__(self, tx_id: _Optional[str] = ..., input_sum: _Optional[int] = ..., output_sum: _Optional[int] = ..., fee: _Optional[int] = ..., size: _Optional[int] = ..., is_pending: bool = ..., memo: _Optional[str] = ...) -> None: ...

class GetNetworkRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetNetworkReply(_message.Message):
    __slots__ = ("network",)
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    network: str
    def __init__(self, network: _Optional[str] = ...) -> None: ...

class GetDaoStatusRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetDaoStatusReply(_message.Message):
    __slots__ = ("is_dao_state_ready_and_in_sync",)
    IS_DAO_STATE_READY_AND_IN_SYNC_FIELD_NUMBER: _ClassVar[int]
    is_dao_state_ready_and_in_sync: bool
    def __init__(self, is_dao_state_ready_and_in_sync: bool = ...) -> None: ...

class GetBalancesRequest(_message.Message):
    __slots__ = ("currency_code",)
    CURRENCY_CODE_FIELD_NUMBER: _ClassVar[int]
    currency_code: str
    def __init__(self, currency_code: _Optional[str] = ...) -> None: ...

class GetBalancesReply(_message.Message):
    __slots__ = ("balances",)
    BALANCES_FIELD_NUMBER: _ClassVar[int]
    balances: BalancesInfo
    def __init__(self, balances: _Optional[_Union[BalancesInfo, _Mapping]] = ...) -> None: ...

class GetAddressBalanceRequest(_message.Message):
    __slots__ = ("address",)
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    address: str
    def __init__(self, address: _Optional[str] = ...) -> None: ...

class GetAddressBalanceReply(_message.Message):
    __slots__ = ("address_balance_info",)
    ADDRESS_BALANCE_INFO_FIELD_NUMBER: _ClassVar[int]
    address_balance_info: AddressBalanceInfo
    def __init__(self, address_balance_info: _Optional[_Union[AddressBalanceInfo, _Mapping]] = ...) -> None: ...

class GetUnusedBsqAddressRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetUnusedBsqAddressReply(_message.Message):
    __slots__ = ("address",)
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    address: str
    def __init__(self, address: _Optional[str] = ...) -> None: ...

class SendBsqRequest(_message.Message):
    __slots__ = ("address", "amount", "tx_fee_rate")
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    TX_FEE_RATE_FIELD_NUMBER: _ClassVar[int]
    address: str
    amount: str
    tx_fee_rate: str
    def __init__(self, address: _Optional[str] = ..., amount: _Optional[str] = ..., tx_fee_rate: _Optional[str] = ...) -> None: ...

class SendBsqReply(_message.Message):
    __slots__ = ("tx_info",)
    TX_INFO_FIELD_NUMBER: _ClassVar[int]
    tx_info: TxInfo
    def __init__(self, tx_info: _Optional[_Union[TxInfo, _Mapping]] = ...) -> None: ...

class SendBtcRequest(_message.Message):
    __slots__ = ("address", "amount", "tx_fee_rate", "memo")
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    TX_FEE_RATE_FIELD_NUMBER: _ClassVar[int]
    MEMO_FIELD_NUMBER: _ClassVar[int]
    address: str
    amount: str
    tx_fee_rate: str
    memo: str
    def __init__(self, address: _Optional[str] = ..., amount: _Optional[str] = ..., tx_fee_rate: _Optional[str] = ..., memo: _Optional[str] = ...) -> None: ...

class SendBtcReply(_message.Message):
    __slots__ = ("tx_info",)
    TX_INFO_FIELD_NUMBER: _ClassVar[int]
    tx_info: TxInfo
    def __init__(self, tx_info: _Optional[_Union[TxInfo, _Mapping]] = ...) -> None: ...

class VerifyBsqSentToAddressRequest(_message.Message):
    __slots__ = ("address", "amount")
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    address: str
    amount: str
    def __init__(self, address: _Optional[str] = ..., amount: _Optional[str] = ...) -> None: ...

class VerifyBsqSentToAddressReply(_message.Message):
    __slots__ = ("is_amount_received",)
    IS_AMOUNT_RECEIVED_FIELD_NUMBER: _ClassVar[int]
    is_amount_received: bool
    def __init__(self, is_amount_received: bool = ...) -> None: ...

class GetTxFeeRateRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetTxFeeRateReply(_message.Message):
    __slots__ = ("tx_fee_rate_info",)
    TX_FEE_RATE_INFO_FIELD_NUMBER: _ClassVar[int]
    tx_fee_rate_info: TxFeeRateInfo
    def __init__(self, tx_fee_rate_info: _Optional[_Union[TxFeeRateInfo, _Mapping]] = ...) -> None: ...

class SetTxFeeRatePreferenceRequest(_message.Message):
    __slots__ = ("tx_fee_rate_preference",)
    TX_FEE_RATE_PREFERENCE_FIELD_NUMBER: _ClassVar[int]
    tx_fee_rate_preference: int
    def __init__(self, tx_fee_rate_preference: _Optional[int] = ...) -> None: ...

class SetTxFeeRatePreferenceReply(_message.Message):
    __slots__ = ("tx_fee_rate_info",)
    TX_FEE_RATE_INFO_FIELD_NUMBER: _ClassVar[int]
    tx_fee_rate_info: TxFeeRateInfo
    def __init__(self, tx_fee_rate_info: _Optional[_Union[TxFeeRateInfo, _Mapping]] = ...) -> None: ...

class UnsetTxFeeRatePreferenceRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UnsetTxFeeRatePreferenceReply(_message.Message):
    __slots__ = ("tx_fee_rate_info",)
    TX_FEE_RATE_INFO_FIELD_NUMBER: _ClassVar[int]
    tx_fee_rate_info: TxFeeRateInfo
    def __init__(self, tx_fee_rate_info: _Optional[_Union[TxFeeRateInfo, _Mapping]] = ...) -> None: ...

class GetTransactionsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetTransactionsReply(_message.Message):
    __slots__ = ("tx_info",)
    TX_INFO_FIELD_NUMBER: _ClassVar[int]
    tx_info: _containers.RepeatedCompositeFieldContainer[TxInfo]
    def __init__(self, tx_info: _Optional[_Iterable[_Union[TxInfo, _Mapping]]] = ...) -> None: ...

class GetTransactionRequest(_message.Message):
    __slots__ = ("tx_id",)
    TX_ID_FIELD_NUMBER: _ClassVar[int]
    tx_id: str
    def __init__(self, tx_id: _Optional[str] = ...) -> None: ...

class GetTransactionReply(_message.Message):
    __slots__ = ("tx_info",)
    TX_INFO_FIELD_NUMBER: _ClassVar[int]
    tx_info: TxInfo
    def __init__(self, tx_info: _Optional[_Union[TxInfo, _Mapping]] = ...) -> None: ...

class GetFundingAddressesRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetFundingAddressesReply(_message.Message):
    __slots__ = ("address_balance_info",)
    ADDRESS_BALANCE_INFO_FIELD_NUMBER: _ClassVar[int]
    address_balance_info: _containers.RepeatedCompositeFieldContainer[AddressBalanceInfo]
    def __init__(self, address_balance_info: _Optional[_Iterable[_Union[AddressBalanceInfo, _Mapping]]] = ...) -> None: ...

class SetWalletPasswordRequest(_message.Message):
    __slots__ = ("password", "new_password")
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    NEW_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    password: str
    new_password: str
    def __init__(self, password: _Optional[str] = ..., new_password: _Optional[str] = ...) -> None: ...

class SetWalletPasswordReply(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RemoveWalletPasswordRequest(_message.Message):
    __slots__ = ("password",)
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    password: str
    def __init__(self, password: _Optional[str] = ...) -> None: ...

class RemoveWalletPasswordReply(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class LockWalletRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class LockWalletReply(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UnlockWalletRequest(_message.Message):
    __slots__ = ("password", "timeout")
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    password: str
    timeout: int
    def __init__(self, password: _Optional[str] = ..., timeout: _Optional[int] = ...) -> None: ...

class UnlockWalletReply(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BalancesInfo(_message.Message):
    __slots__ = ("bsq", "btc")
    BSQ_FIELD_NUMBER: _ClassVar[int]
    BTC_FIELD_NUMBER: _ClassVar[int]
    bsq: BsqBalanceInfo
    btc: BtcBalanceInfo
    def __init__(self, bsq: _Optional[_Union[BsqBalanceInfo, _Mapping]] = ..., btc: _Optional[_Union[BtcBalanceInfo, _Mapping]] = ...) -> None: ...

class BsqBalanceInfo(_message.Message):
    __slots__ = ("available_confirmed_balance", "unverified_balance", "unconfirmed_change_balance", "locked_for_voting_balance", "lockup_bonds_balance", "unlocking_bonds_balance")
    AVAILABLE_CONFIRMED_BALANCE_FIELD_NUMBER: _ClassVar[int]
    UNVERIFIED_BALANCE_FIELD_NUMBER: _ClassVar[int]
    UNCONFIRMED_CHANGE_BALANCE_FIELD_NUMBER: _ClassVar[int]
    LOCKED_FOR_VOTING_BALANCE_FIELD_NUMBER: _ClassVar[int]
    LOCKUP_BONDS_BALANCE_FIELD_NUMBER: _ClassVar[int]
    UNLOCKING_BONDS_BALANCE_FIELD_NUMBER: _ClassVar[int]
    available_confirmed_balance: int
    unverified_balance: int
    unconfirmed_change_balance: int
    locked_for_voting_balance: int
    lockup_bonds_balance: int
    unlocking_bonds_balance: int
    def __init__(self, available_confirmed_balance: _Optional[int] = ..., unverified_balance: _Optional[int] = ..., unconfirmed_change_balance: _Optional[int] = ..., locked_for_voting_balance: _Optional[int] = ..., lockup_bonds_balance: _Optional[int] = ..., unlocking_bonds_balance: _Optional[int] = ...) -> None: ...

class BtcBalanceInfo(_message.Message):
    __slots__ = ("available_balance", "reserved_balance", "total_available_balance", "locked_balance")
    AVAILABLE_BALANCE_FIELD_NUMBER: _ClassVar[int]
    RESERVED_BALANCE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_AVAILABLE_BALANCE_FIELD_NUMBER: _ClassVar[int]
    LOCKED_BALANCE_FIELD_NUMBER: _ClassVar[int]
    available_balance: int
    reserved_balance: int
    total_available_balance: int
    locked_balance: int
    def __init__(self, available_balance: _Optional[int] = ..., reserved_balance: _Optional[int] = ..., total_available_balance: _Optional[int] = ..., locked_balance: _Optional[int] = ...) -> None: ...

class AddressBalanceInfo(_message.Message):
    __slots__ = ("address", "balance", "num_confirmations", "is_address_unused")
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    BALANCE_FIELD_NUMBER: _ClassVar[int]
    NUM_CONFIRMATIONS_FIELD_NUMBER: _ClassVar[int]
    IS_ADDRESS_UNUSED_FIELD_NUMBER: _ClassVar[int]
    address: str
    balance: int
    num_confirmations: int
    is_address_unused: bool
    def __init__(self, address: _Optional[str] = ..., balance: _Optional[int] = ..., num_confirmations: _Optional[int] = ..., is_address_unused: bool = ...) -> None: ...

class GetVersionRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetVersionReply(_message.Message):
    __slots__ = ("version",)
    VERSION_FIELD_NUMBER: _ClassVar[int]
    version: str
    def __init__(self, version: _Optional[str] = ...) -> None: ...
