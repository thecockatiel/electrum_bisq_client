from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SupportType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ARBITRATION: _ClassVar[SupportType]
    MEDIATION: _ClassVar[SupportType]
    TRADE: _ClassVar[SupportType]
    REFUND: _ClassVar[SupportType]

class OfferDirection(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OFFER_DIRECTION_ERROR: _ClassVar[OfferDirection]
    BUY: _ClassVar[OfferDirection]
    SELL: _ClassVar[OfferDirection]

class AvailabilityResult(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PB_ERROR: _ClassVar[AvailabilityResult]
    UNKNOWN_FAILURE: _ClassVar[AvailabilityResult]
    AVAILABLE: _ClassVar[AvailabilityResult]
    OFFER_TAKEN: _ClassVar[AvailabilityResult]
    PRICE_OUT_OF_TOLERANCE: _ClassVar[AvailabilityResult]
    MARKET_PRICE_NOT_AVAILABLE: _ClassVar[AvailabilityResult]
    NO_ARBITRATORS: _ClassVar[AvailabilityResult]
    NO_MEDIATORS: _ClassVar[AvailabilityResult]
    USER_IGNORED: _ClassVar[AvailabilityResult]
    MISSING_MANDATORY_CAPABILITY: _ClassVar[AvailabilityResult]
    NO_REFUND_AGENTS: _ClassVar[AvailabilityResult]
    UNCONF_TX_LIMIT_HIT: _ClassVar[AvailabilityResult]
    MAKER_DENIED_API_USER: _ClassVar[AvailabilityResult]
    PRICE_CHECK_FAILED: _ClassVar[AvailabilityResult]
    INVALID_SNAPSHOT_HEIGHT: _ClassVar[AvailabilityResult]

class MediationResultState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PB_ERROR_MEDIATION_RESULT: _ClassVar[MediationResultState]
    UNDEFINED_MEDIATION_RESULT: _ClassVar[MediationResultState]
    MEDIATION_RESULT_ACCEPTED: _ClassVar[MediationResultState]
    MEDIATION_RESULT_REJECTED: _ClassVar[MediationResultState]
    SIG_MSG_SENT: _ClassVar[MediationResultState]
    SIG_MSG_ARRIVED: _ClassVar[MediationResultState]
    SIG_MSG_IN_MAILBOX: _ClassVar[MediationResultState]
    SIG_MSG_SEND_FAILED: _ClassVar[MediationResultState]
    RECEIVED_SIG_MSG: _ClassVar[MediationResultState]
    PAYOUT_TX_PUBLISHED: _ClassVar[MediationResultState]
    PAYOUT_TX_PUBLISHED_MSG_SENT: _ClassVar[MediationResultState]
    PAYOUT_TX_PUBLISHED_MSG_ARRIVED: _ClassVar[MediationResultState]
    PAYOUT_TX_PUBLISHED_MSG_IN_MAILBOX: _ClassVar[MediationResultState]
    PAYOUT_TX_PUBLISHED_MSG_SEND_FAILED: _ClassVar[MediationResultState]
    RECEIVED_PAYOUT_TX_PUBLISHED_MSG: _ClassVar[MediationResultState]
    PAYOUT_TX_SEEN_IN_NETWORK: _ClassVar[MediationResultState]

class RefundResultState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PB_ERROR_REFUND_RESULT: _ClassVar[RefundResultState]
    UNDEFINED_REFUND_RESULT: _ClassVar[RefundResultState]

class TxType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PB_ERROR_TX_TYPE: _ClassVar[TxType]
    UNDEFINED_TX_TYPE: _ClassVar[TxType]
    UNVERIFIED: _ClassVar[TxType]
    INVALID: _ClassVar[TxType]
    GENESIS: _ClassVar[TxType]
    TRANSFER_BSQ: _ClassVar[TxType]
    PAY_TRADE_FEE: _ClassVar[TxType]
    PROPOSAL: _ClassVar[TxType]
    COMPENSATION_REQUEST: _ClassVar[TxType]
    REIMBURSEMENT_REQUEST: _ClassVar[TxType]
    BLIND_VOTE: _ClassVar[TxType]
    VOTE_REVEAL: _ClassVar[TxType]
    LOCKUP: _ClassVar[TxType]
    UNLOCK: _ClassVar[TxType]
    ASSET_LISTING_FEE: _ClassVar[TxType]
    PROOF_OF_BURN: _ClassVar[TxType]
    IRREGULAR: _ClassVar[TxType]

class TxOutputType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PB_ERROR_TX_OUTPUT_TYPE: _ClassVar[TxOutputType]
    UNDEFINED_OUTPUT: _ClassVar[TxOutputType]
    GENESIS_OUTPUT: _ClassVar[TxOutputType]
    BSQ_OUTPUT: _ClassVar[TxOutputType]
    BTC_OUTPUT: _ClassVar[TxOutputType]
    PROPOSAL_OP_RETURN_OUTPUT: _ClassVar[TxOutputType]
    COMP_REQ_OP_RETURN_OUTPUT: _ClassVar[TxOutputType]
    REIMBURSEMENT_OP_RETURN_OUTPUT: _ClassVar[TxOutputType]
    CONFISCATE_BOND_OP_RETURN_OUTPUT: _ClassVar[TxOutputType]
    ISSUANCE_CANDIDATE_OUTPUT: _ClassVar[TxOutputType]
    BLIND_VOTE_LOCK_STAKE_OUTPUT: _ClassVar[TxOutputType]
    BLIND_VOTE_OP_RETURN_OUTPUT: _ClassVar[TxOutputType]
    VOTE_REVEAL_UNLOCK_STAKE_OUTPUT: _ClassVar[TxOutputType]
    VOTE_REVEAL_OP_RETURN_OUTPUT: _ClassVar[TxOutputType]
    ASSET_LISTING_FEE_OP_RETURN_OUTPUT: _ClassVar[TxOutputType]
    PROOF_OF_BURN_OP_RETURN_OUTPUT: _ClassVar[TxOutputType]
    LOCKUP_OUTPUT: _ClassVar[TxOutputType]
    LOCKUP_OP_RETURN_OUTPUT: _ClassVar[TxOutputType]
    UNLOCK_OUTPUT: _ClassVar[TxOutputType]
    INVALID_OUTPUT: _ClassVar[TxOutputType]

class ScriptType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PB_ERROR_SCRIPT_TYPES: _ClassVar[ScriptType]
    PUB_KEY: _ClassVar[ScriptType]
    PUB_KEY_HASH: _ClassVar[ScriptType]
    SCRIPT_HASH: _ClassVar[ScriptType]
    MULTISIG: _ClassVar[ScriptType]
    NULL_DATA: _ClassVar[ScriptType]
    WITNESS_V0_KEYHASH: _ClassVar[ScriptType]
    WITNESS_V0_SCRIPTHASH: _ClassVar[ScriptType]
    NONSTANDARD: _ClassVar[ScriptType]
    WITNESS_UNKNOWN: _ClassVar[ScriptType]
    WITNESS_V1_TAPROOT: _ClassVar[ScriptType]
ARBITRATION: SupportType
MEDIATION: SupportType
TRADE: SupportType
REFUND: SupportType
OFFER_DIRECTION_ERROR: OfferDirection
BUY: OfferDirection
SELL: OfferDirection
PB_ERROR: AvailabilityResult
UNKNOWN_FAILURE: AvailabilityResult
AVAILABLE: AvailabilityResult
OFFER_TAKEN: AvailabilityResult
PRICE_OUT_OF_TOLERANCE: AvailabilityResult
MARKET_PRICE_NOT_AVAILABLE: AvailabilityResult
NO_ARBITRATORS: AvailabilityResult
NO_MEDIATORS: AvailabilityResult
USER_IGNORED: AvailabilityResult
MISSING_MANDATORY_CAPABILITY: AvailabilityResult
NO_REFUND_AGENTS: AvailabilityResult
UNCONF_TX_LIMIT_HIT: AvailabilityResult
MAKER_DENIED_API_USER: AvailabilityResult
PRICE_CHECK_FAILED: AvailabilityResult
INVALID_SNAPSHOT_HEIGHT: AvailabilityResult
PB_ERROR_MEDIATION_RESULT: MediationResultState
UNDEFINED_MEDIATION_RESULT: MediationResultState
MEDIATION_RESULT_ACCEPTED: MediationResultState
MEDIATION_RESULT_REJECTED: MediationResultState
SIG_MSG_SENT: MediationResultState
SIG_MSG_ARRIVED: MediationResultState
SIG_MSG_IN_MAILBOX: MediationResultState
SIG_MSG_SEND_FAILED: MediationResultState
RECEIVED_SIG_MSG: MediationResultState
PAYOUT_TX_PUBLISHED: MediationResultState
PAYOUT_TX_PUBLISHED_MSG_SENT: MediationResultState
PAYOUT_TX_PUBLISHED_MSG_ARRIVED: MediationResultState
PAYOUT_TX_PUBLISHED_MSG_IN_MAILBOX: MediationResultState
PAYOUT_TX_PUBLISHED_MSG_SEND_FAILED: MediationResultState
RECEIVED_PAYOUT_TX_PUBLISHED_MSG: MediationResultState
PAYOUT_TX_SEEN_IN_NETWORK: MediationResultState
PB_ERROR_REFUND_RESULT: RefundResultState
UNDEFINED_REFUND_RESULT: RefundResultState
PB_ERROR_TX_TYPE: TxType
UNDEFINED_TX_TYPE: TxType
UNVERIFIED: TxType
INVALID: TxType
GENESIS: TxType
TRANSFER_BSQ: TxType
PAY_TRADE_FEE: TxType
PROPOSAL: TxType
COMPENSATION_REQUEST: TxType
REIMBURSEMENT_REQUEST: TxType
BLIND_VOTE: TxType
VOTE_REVEAL: TxType
LOCKUP: TxType
UNLOCK: TxType
ASSET_LISTING_FEE: TxType
PROOF_OF_BURN: TxType
IRREGULAR: TxType
PB_ERROR_TX_OUTPUT_TYPE: TxOutputType
UNDEFINED_OUTPUT: TxOutputType
GENESIS_OUTPUT: TxOutputType
BSQ_OUTPUT: TxOutputType
BTC_OUTPUT: TxOutputType
PROPOSAL_OP_RETURN_OUTPUT: TxOutputType
COMP_REQ_OP_RETURN_OUTPUT: TxOutputType
REIMBURSEMENT_OP_RETURN_OUTPUT: TxOutputType
CONFISCATE_BOND_OP_RETURN_OUTPUT: TxOutputType
ISSUANCE_CANDIDATE_OUTPUT: TxOutputType
BLIND_VOTE_LOCK_STAKE_OUTPUT: TxOutputType
BLIND_VOTE_OP_RETURN_OUTPUT: TxOutputType
VOTE_REVEAL_UNLOCK_STAKE_OUTPUT: TxOutputType
VOTE_REVEAL_OP_RETURN_OUTPUT: TxOutputType
ASSET_LISTING_FEE_OP_RETURN_OUTPUT: TxOutputType
PROOF_OF_BURN_OP_RETURN_OUTPUT: TxOutputType
LOCKUP_OUTPUT: TxOutputType
LOCKUP_OP_RETURN_OUTPUT: TxOutputType
UNLOCK_OUTPUT: TxOutputType
INVALID_OUTPUT: TxOutputType
PB_ERROR_SCRIPT_TYPES: ScriptType
PUB_KEY: ScriptType
PUB_KEY_HASH: ScriptType
SCRIPT_HASH: ScriptType
MULTISIG: ScriptType
NULL_DATA: ScriptType
WITNESS_V0_KEYHASH: ScriptType
WITNESS_V0_SCRIPTHASH: ScriptType
NONSTANDARD: ScriptType
WITNESS_UNKNOWN: ScriptType
WITNESS_V1_TAPROOT: ScriptType

class NetworkEnvelope(_message.Message):
    __slots__ = ("message_version", "preliminary_get_data_request", "get_data_response", "get_updated_data_request", "get_peers_request", "get_peers_response", "ping", "pong", "offer_availability_request", "offer_availability_response", "refresh_offer_message", "add_data_message", "remove_data_message", "remove_mailbox_data_message", "close_connection_message", "prefixed_sealed_and_signed_message", "inputs_for_deposit_tx_request", "inputs_for_deposit_tx_response", "deposit_tx_message", "counter_currency_transfer_started_message", "payout_tx_published_message", "open_new_dispute_message", "peer_opened_dispute_message", "chat_message", "dispute_result_message", "peer_published_dispute_payout_tx_message", "private_notification_message", "get_blocks_request", "get_blocks_response", "new_block_broadcast_message", "add_persistable_network_payload_message", "ack_message", "republish_governance_data_request", "new_dao_state_hash_message", "get_dao_state_hashes_request", "get_dao_state_hashes_response", "new_proposal_state_hash_message", "get_proposal_state_hashes_request", "get_proposal_state_hashes_response", "new_blind_vote_state_hash_message", "get_blind_vote_state_hashes_request", "get_blind_vote_state_hashes_response", "bundle_of_envelopes", "mediated_payout_tx_signature_message", "mediated_payout_tx_published_message", "delayed_payout_tx_signature_request", "delayed_payout_tx_signature_response", "deposit_tx_and_delayed_payout_tx_message", "peer_published_delayed_payout_tx_message", "refresh_trade_state_request", "trader_signed_witness_message", "get_inventory_request", "get_inventory_response", "share_buyer_payment_account_message", "sellers_bsq_swap_request", "buyers_bsq_swap_request", "bsq_swap_tx_inputs_message", "bsq_swap_finalize_tx_request", "bsq_swap_finalized_tx_message", "file_transfer_part", "get_accounting_blocks_request", "get_accounting_blocks_response", "new_accounting_block_broadcast_message")
    MESSAGE_VERSION_FIELD_NUMBER: _ClassVar[int]
    PRELIMINARY_GET_DATA_REQUEST_FIELD_NUMBER: _ClassVar[int]
    GET_DATA_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    GET_UPDATED_DATA_REQUEST_FIELD_NUMBER: _ClassVar[int]
    GET_PEERS_REQUEST_FIELD_NUMBER: _ClassVar[int]
    GET_PEERS_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    PING_FIELD_NUMBER: _ClassVar[int]
    PONG_FIELD_NUMBER: _ClassVar[int]
    OFFER_AVAILABILITY_REQUEST_FIELD_NUMBER: _ClassVar[int]
    OFFER_AVAILABILITY_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    REFRESH_OFFER_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ADD_DATA_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REMOVE_DATA_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REMOVE_MAILBOX_DATA_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CLOSE_CONNECTION_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    PREFIXED_SEALED_AND_SIGNED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    INPUTS_FOR_DEPOSIT_TX_REQUEST_FIELD_NUMBER: _ClassVar[int]
    INPUTS_FOR_DEPOSIT_TX_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    DEPOSIT_TX_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    COUNTER_CURRENCY_TRANSFER_STARTED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    PAYOUT_TX_PUBLISHED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    OPEN_NEW_DISPUTE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    PEER_OPENED_DISPUTE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CHAT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    DISPUTE_RESULT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    PEER_PUBLISHED_DISPUTE_PAYOUT_TX_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_NOTIFICATION_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    GET_BLOCKS_REQUEST_FIELD_NUMBER: _ClassVar[int]
    GET_BLOCKS_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    NEW_BLOCK_BROADCAST_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ADD_PERSISTABLE_NETWORK_PAYLOAD_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ACK_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REPUBLISH_GOVERNANCE_DATA_REQUEST_FIELD_NUMBER: _ClassVar[int]
    NEW_DAO_STATE_HASH_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    GET_DAO_STATE_HASHES_REQUEST_FIELD_NUMBER: _ClassVar[int]
    GET_DAO_STATE_HASHES_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    NEW_PROPOSAL_STATE_HASH_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    GET_PROPOSAL_STATE_HASHES_REQUEST_FIELD_NUMBER: _ClassVar[int]
    GET_PROPOSAL_STATE_HASHES_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    NEW_BLIND_VOTE_STATE_HASH_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    GET_BLIND_VOTE_STATE_HASHES_REQUEST_FIELD_NUMBER: _ClassVar[int]
    GET_BLIND_VOTE_STATE_HASHES_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    BUNDLE_OF_ENVELOPES_FIELD_NUMBER: _ClassVar[int]
    MEDIATED_PAYOUT_TX_SIGNATURE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    MEDIATED_PAYOUT_TX_PUBLISHED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    DELAYED_PAYOUT_TX_SIGNATURE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    DELAYED_PAYOUT_TX_SIGNATURE_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    DEPOSIT_TX_AND_DELAYED_PAYOUT_TX_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    PEER_PUBLISHED_DELAYED_PAYOUT_TX_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TRADE_STATE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    TRADER_SIGNED_WITNESS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    GET_INVENTORY_REQUEST_FIELD_NUMBER: _ClassVar[int]
    GET_INVENTORY_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    SHARE_BUYER_PAYMENT_ACCOUNT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SELLERS_BSQ_SWAP_REQUEST_FIELD_NUMBER: _ClassVar[int]
    BUYERS_BSQ_SWAP_REQUEST_FIELD_NUMBER: _ClassVar[int]
    BSQ_SWAP_TX_INPUTS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    BSQ_SWAP_FINALIZE_TX_REQUEST_FIELD_NUMBER: _ClassVar[int]
    BSQ_SWAP_FINALIZED_TX_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    FILE_TRANSFER_PART_FIELD_NUMBER: _ClassVar[int]
    GET_ACCOUNTING_BLOCKS_REQUEST_FIELD_NUMBER: _ClassVar[int]
    GET_ACCOUNTING_BLOCKS_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    NEW_ACCOUNTING_BLOCK_BROADCAST_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message_version: int
    preliminary_get_data_request: PreliminaryGetDataRequest
    get_data_response: GetDataResponse
    get_updated_data_request: GetUpdatedDataRequest
    get_peers_request: GetPeersRequest
    get_peers_response: GetPeersResponse
    ping: Ping
    pong: Pong
    offer_availability_request: OfferAvailabilityRequest
    offer_availability_response: OfferAvailabilityResponse
    refresh_offer_message: RefreshOfferMessage
    add_data_message: AddDataMessage
    remove_data_message: RemoveDataMessage
    remove_mailbox_data_message: RemoveMailboxDataMessage
    close_connection_message: CloseConnectionMessage
    prefixed_sealed_and_signed_message: PrefixedSealedAndSignedMessage
    inputs_for_deposit_tx_request: InputsForDepositTxRequest
    inputs_for_deposit_tx_response: InputsForDepositTxResponse
    deposit_tx_message: DepositTxMessage
    counter_currency_transfer_started_message: CounterCurrencyTransferStartedMessage
    payout_tx_published_message: PayoutTxPublishedMessage
    open_new_dispute_message: OpenNewDisputeMessage
    peer_opened_dispute_message: PeerOpenedDisputeMessage
    chat_message: ChatMessage
    dispute_result_message: DisputeResultMessage
    peer_published_dispute_payout_tx_message: PeerPublishedDisputePayoutTxMessage
    private_notification_message: PrivateNotificationMessage
    get_blocks_request: GetBlocksRequest
    get_blocks_response: GetBlocksResponse
    new_block_broadcast_message: NewBlockBroadcastMessage
    add_persistable_network_payload_message: AddPersistableNetworkPayloadMessage
    ack_message: AckMessage
    republish_governance_data_request: RepublishGovernanceDataRequest
    new_dao_state_hash_message: NewDaoStateHashMessage
    get_dao_state_hashes_request: GetDaoStateHashesRequest
    get_dao_state_hashes_response: GetDaoStateHashesResponse
    new_proposal_state_hash_message: NewProposalStateHashMessage
    get_proposal_state_hashes_request: GetProposalStateHashesRequest
    get_proposal_state_hashes_response: GetProposalStateHashesResponse
    new_blind_vote_state_hash_message: NewBlindVoteStateHashMessage
    get_blind_vote_state_hashes_request: GetBlindVoteStateHashesRequest
    get_blind_vote_state_hashes_response: GetBlindVoteStateHashesResponse
    bundle_of_envelopes: BundleOfEnvelopes
    mediated_payout_tx_signature_message: MediatedPayoutTxSignatureMessage
    mediated_payout_tx_published_message: MediatedPayoutTxPublishedMessage
    delayed_payout_tx_signature_request: DelayedPayoutTxSignatureRequest
    delayed_payout_tx_signature_response: DelayedPayoutTxSignatureResponse
    deposit_tx_and_delayed_payout_tx_message: DepositTxAndDelayedPayoutTxMessage
    peer_published_delayed_payout_tx_message: PeerPublishedDelayedPayoutTxMessage
    refresh_trade_state_request: RefreshTradeStateRequest
    trader_signed_witness_message: TraderSignedWitnessMessage
    get_inventory_request: GetInventoryRequest
    get_inventory_response: GetInventoryResponse
    share_buyer_payment_account_message: ShareBuyerPaymentAccountMessage
    sellers_bsq_swap_request: SellersBsqSwapRequest
    buyers_bsq_swap_request: BuyersBsqSwapRequest
    bsq_swap_tx_inputs_message: BsqSwapTxInputsMessage
    bsq_swap_finalize_tx_request: BsqSwapFinalizeTxRequest
    bsq_swap_finalized_tx_message: BsqSwapFinalizedTxMessage
    file_transfer_part: FileTransferPart
    get_accounting_blocks_request: GetAccountingBlocksRequest
    get_accounting_blocks_response: GetAccountingBlocksResponse
    new_accounting_block_broadcast_message: NewAccountingBlockBroadcastMessage
    def __init__(self, message_version: _Optional[int] = ..., preliminary_get_data_request: _Optional[_Union[PreliminaryGetDataRequest, _Mapping]] = ..., get_data_response: _Optional[_Union[GetDataResponse, _Mapping]] = ..., get_updated_data_request: _Optional[_Union[GetUpdatedDataRequest, _Mapping]] = ..., get_peers_request: _Optional[_Union[GetPeersRequest, _Mapping]] = ..., get_peers_response: _Optional[_Union[GetPeersResponse, _Mapping]] = ..., ping: _Optional[_Union[Ping, _Mapping]] = ..., pong: _Optional[_Union[Pong, _Mapping]] = ..., offer_availability_request: _Optional[_Union[OfferAvailabilityRequest, _Mapping]] = ..., offer_availability_response: _Optional[_Union[OfferAvailabilityResponse, _Mapping]] = ..., refresh_offer_message: _Optional[_Union[RefreshOfferMessage, _Mapping]] = ..., add_data_message: _Optional[_Union[AddDataMessage, _Mapping]] = ..., remove_data_message: _Optional[_Union[RemoveDataMessage, _Mapping]] = ..., remove_mailbox_data_message: _Optional[_Union[RemoveMailboxDataMessage, _Mapping]] = ..., close_connection_message: _Optional[_Union[CloseConnectionMessage, _Mapping]] = ..., prefixed_sealed_and_signed_message: _Optional[_Union[PrefixedSealedAndSignedMessage, _Mapping]] = ..., inputs_for_deposit_tx_request: _Optional[_Union[InputsForDepositTxRequest, _Mapping]] = ..., inputs_for_deposit_tx_response: _Optional[_Union[InputsForDepositTxResponse, _Mapping]] = ..., deposit_tx_message: _Optional[_Union[DepositTxMessage, _Mapping]] = ..., counter_currency_transfer_started_message: _Optional[_Union[CounterCurrencyTransferStartedMessage, _Mapping]] = ..., payout_tx_published_message: _Optional[_Union[PayoutTxPublishedMessage, _Mapping]] = ..., open_new_dispute_message: _Optional[_Union[OpenNewDisputeMessage, _Mapping]] = ..., peer_opened_dispute_message: _Optional[_Union[PeerOpenedDisputeMessage, _Mapping]] = ..., chat_message: _Optional[_Union[ChatMessage, _Mapping]] = ..., dispute_result_message: _Optional[_Union[DisputeResultMessage, _Mapping]] = ..., peer_published_dispute_payout_tx_message: _Optional[_Union[PeerPublishedDisputePayoutTxMessage, _Mapping]] = ..., private_notification_message: _Optional[_Union[PrivateNotificationMessage, _Mapping]] = ..., get_blocks_request: _Optional[_Union[GetBlocksRequest, _Mapping]] = ..., get_blocks_response: _Optional[_Union[GetBlocksResponse, _Mapping]] = ..., new_block_broadcast_message: _Optional[_Union[NewBlockBroadcastMessage, _Mapping]] = ..., add_persistable_network_payload_message: _Optional[_Union[AddPersistableNetworkPayloadMessage, _Mapping]] = ..., ack_message: _Optional[_Union[AckMessage, _Mapping]] = ..., republish_governance_data_request: _Optional[_Union[RepublishGovernanceDataRequest, _Mapping]] = ..., new_dao_state_hash_message: _Optional[_Union[NewDaoStateHashMessage, _Mapping]] = ..., get_dao_state_hashes_request: _Optional[_Union[GetDaoStateHashesRequest, _Mapping]] = ..., get_dao_state_hashes_response: _Optional[_Union[GetDaoStateHashesResponse, _Mapping]] = ..., new_proposal_state_hash_message: _Optional[_Union[NewProposalStateHashMessage, _Mapping]] = ..., get_proposal_state_hashes_request: _Optional[_Union[GetProposalStateHashesRequest, _Mapping]] = ..., get_proposal_state_hashes_response: _Optional[_Union[GetProposalStateHashesResponse, _Mapping]] = ..., new_blind_vote_state_hash_message: _Optional[_Union[NewBlindVoteStateHashMessage, _Mapping]] = ..., get_blind_vote_state_hashes_request: _Optional[_Union[GetBlindVoteStateHashesRequest, _Mapping]] = ..., get_blind_vote_state_hashes_response: _Optional[_Union[GetBlindVoteStateHashesResponse, _Mapping]] = ..., bundle_of_envelopes: _Optional[_Union[BundleOfEnvelopes, _Mapping]] = ..., mediated_payout_tx_signature_message: _Optional[_Union[MediatedPayoutTxSignatureMessage, _Mapping]] = ..., mediated_payout_tx_published_message: _Optional[_Union[MediatedPayoutTxPublishedMessage, _Mapping]] = ..., delayed_payout_tx_signature_request: _Optional[_Union[DelayedPayoutTxSignatureRequest, _Mapping]] = ..., delayed_payout_tx_signature_response: _Optional[_Union[DelayedPayoutTxSignatureResponse, _Mapping]] = ..., deposit_tx_and_delayed_payout_tx_message: _Optional[_Union[DepositTxAndDelayedPayoutTxMessage, _Mapping]] = ..., peer_published_delayed_payout_tx_message: _Optional[_Union[PeerPublishedDelayedPayoutTxMessage, _Mapping]] = ..., refresh_trade_state_request: _Optional[_Union[RefreshTradeStateRequest, _Mapping]] = ..., trader_signed_witness_message: _Optional[_Union[TraderSignedWitnessMessage, _Mapping]] = ..., get_inventory_request: _Optional[_Union[GetInventoryRequest, _Mapping]] = ..., get_inventory_response: _Optional[_Union[GetInventoryResponse, _Mapping]] = ..., share_buyer_payment_account_message: _Optional[_Union[ShareBuyerPaymentAccountMessage, _Mapping]] = ..., sellers_bsq_swap_request: _Optional[_Union[SellersBsqSwapRequest, _Mapping]] = ..., buyers_bsq_swap_request: _Optional[_Union[BuyersBsqSwapRequest, _Mapping]] = ..., bsq_swap_tx_inputs_message: _Optional[_Union[BsqSwapTxInputsMessage, _Mapping]] = ..., bsq_swap_finalize_tx_request: _Optional[_Union[BsqSwapFinalizeTxRequest, _Mapping]] = ..., bsq_swap_finalized_tx_message: _Optional[_Union[BsqSwapFinalizedTxMessage, _Mapping]] = ..., file_transfer_part: _Optional[_Union[FileTransferPart, _Mapping]] = ..., get_accounting_blocks_request: _Optional[_Union[GetAccountingBlocksRequest, _Mapping]] = ..., get_accounting_blocks_response: _Optional[_Union[GetAccountingBlocksResponse, _Mapping]] = ..., new_accounting_block_broadcast_message: _Optional[_Union[NewAccountingBlockBroadcastMessage, _Mapping]] = ...) -> None: ...

class BundleOfEnvelopes(_message.Message):
    __slots__ = ("envelopes",)
    ENVELOPES_FIELD_NUMBER: _ClassVar[int]
    envelopes: _containers.RepeatedCompositeFieldContainer[NetworkEnvelope]
    def __init__(self, envelopes: _Optional[_Iterable[_Union[NetworkEnvelope, _Mapping]]] = ...) -> None: ...

class PreliminaryGetDataRequest(_message.Message):
    __slots__ = ("nonce", "excluded_keys", "supported_capabilities", "version")
    NONCE_FIELD_NUMBER: _ClassVar[int]
    EXCLUDED_KEYS_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    nonce: int
    excluded_keys: _containers.RepeatedScalarFieldContainer[bytes]
    supported_capabilities: _containers.RepeatedScalarFieldContainer[int]
    version: str
    def __init__(self, nonce: _Optional[int] = ..., excluded_keys: _Optional[_Iterable[bytes]] = ..., supported_capabilities: _Optional[_Iterable[int]] = ..., version: _Optional[str] = ...) -> None: ...

class GetDataResponse(_message.Message):
    __slots__ = ("request_nonce", "is_get_updated_data_response", "data_set", "supported_capabilities", "persistable_network_payload_items", "was_truncated")
    REQUEST_NONCE_FIELD_NUMBER: _ClassVar[int]
    IS_GET_UPDATED_DATA_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    DATA_SET_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    PERSISTABLE_NETWORK_PAYLOAD_ITEMS_FIELD_NUMBER: _ClassVar[int]
    WAS_TRUNCATED_FIELD_NUMBER: _ClassVar[int]
    request_nonce: int
    is_get_updated_data_response: bool
    data_set: _containers.RepeatedCompositeFieldContainer[StorageEntryWrapper]
    supported_capabilities: _containers.RepeatedScalarFieldContainer[int]
    persistable_network_payload_items: _containers.RepeatedCompositeFieldContainer[PersistableNetworkPayload]
    was_truncated: bool
    def __init__(self, request_nonce: _Optional[int] = ..., is_get_updated_data_response: bool = ..., data_set: _Optional[_Iterable[_Union[StorageEntryWrapper, _Mapping]]] = ..., supported_capabilities: _Optional[_Iterable[int]] = ..., persistable_network_payload_items: _Optional[_Iterable[_Union[PersistableNetworkPayload, _Mapping]]] = ..., was_truncated: bool = ...) -> None: ...

class GetUpdatedDataRequest(_message.Message):
    __slots__ = ("sender_node_address", "nonce", "excluded_keys", "version")
    SENDER_NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    NONCE_FIELD_NUMBER: _ClassVar[int]
    EXCLUDED_KEYS_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    sender_node_address: NodeAddress
    nonce: int
    excluded_keys: _containers.RepeatedScalarFieldContainer[bytes]
    version: str
    def __init__(self, sender_node_address: _Optional[_Union[NodeAddress, _Mapping]] = ..., nonce: _Optional[int] = ..., excluded_keys: _Optional[_Iterable[bytes]] = ..., version: _Optional[str] = ...) -> None: ...

class FileTransferPart(_message.Message):
    __slots__ = ("sender_node_address", "uid", "trade_id", "trader_id", "seq_num_or_file_length", "message_data")
    SENDER_NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    TRADE_ID_FIELD_NUMBER: _ClassVar[int]
    TRADER_ID_FIELD_NUMBER: _ClassVar[int]
    SEQ_NUM_OR_FILE_LENGTH_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_DATA_FIELD_NUMBER: _ClassVar[int]
    sender_node_address: NodeAddress
    uid: str
    trade_id: str
    trader_id: int
    seq_num_or_file_length: int
    message_data: bytes
    def __init__(self, sender_node_address: _Optional[_Union[NodeAddress, _Mapping]] = ..., uid: _Optional[str] = ..., trade_id: _Optional[str] = ..., trader_id: _Optional[int] = ..., seq_num_or_file_length: _Optional[int] = ..., message_data: _Optional[bytes] = ...) -> None: ...

class GetPeersRequest(_message.Message):
    __slots__ = ("sender_node_address", "nonce", "supported_capabilities", "reported_peers")
    SENDER_NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    NONCE_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    REPORTED_PEERS_FIELD_NUMBER: _ClassVar[int]
    sender_node_address: NodeAddress
    nonce: int
    supported_capabilities: _containers.RepeatedScalarFieldContainer[int]
    reported_peers: _containers.RepeatedCompositeFieldContainer[Peer]
    def __init__(self, sender_node_address: _Optional[_Union[NodeAddress, _Mapping]] = ..., nonce: _Optional[int] = ..., supported_capabilities: _Optional[_Iterable[int]] = ..., reported_peers: _Optional[_Iterable[_Union[Peer, _Mapping]]] = ...) -> None: ...

class GetPeersResponse(_message.Message):
    __slots__ = ("request_nonce", "reported_peers", "supported_capabilities")
    REQUEST_NONCE_FIELD_NUMBER: _ClassVar[int]
    REPORTED_PEERS_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    request_nonce: int
    reported_peers: _containers.RepeatedCompositeFieldContainer[Peer]
    supported_capabilities: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, request_nonce: _Optional[int] = ..., reported_peers: _Optional[_Iterable[_Union[Peer, _Mapping]]] = ..., supported_capabilities: _Optional[_Iterable[int]] = ...) -> None: ...

class Ping(_message.Message):
    __slots__ = ("nonce", "last_round_trip_time")
    NONCE_FIELD_NUMBER: _ClassVar[int]
    LAST_ROUND_TRIP_TIME_FIELD_NUMBER: _ClassVar[int]
    nonce: int
    last_round_trip_time: int
    def __init__(self, nonce: _Optional[int] = ..., last_round_trip_time: _Optional[int] = ...) -> None: ...

class Pong(_message.Message):
    __slots__ = ("request_nonce",)
    REQUEST_NONCE_FIELD_NUMBER: _ClassVar[int]
    request_nonce: int
    def __init__(self, request_nonce: _Optional[int] = ...) -> None: ...

class GetInventoryRequest(_message.Message):
    __slots__ = ("version",)
    VERSION_FIELD_NUMBER: _ClassVar[int]
    version: str
    def __init__(self, version: _Optional[str] = ...) -> None: ...

class GetInventoryResponse(_message.Message):
    __slots__ = ("inventory",)
    class InventoryEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    INVENTORY_FIELD_NUMBER: _ClassVar[int]
    inventory: _containers.ScalarMap[str, str]
    def __init__(self, inventory: _Optional[_Mapping[str, str]] = ...) -> None: ...

class OfferAvailabilityRequest(_message.Message):
    __slots__ = ("offer_id", "pub_key_ring", "takers_trade_price", "supported_capabilities", "uid", "is_taker_api_user", "burning_man_selection_height")
    OFFER_ID_FIELD_NUMBER: _ClassVar[int]
    PUB_KEY_RING_FIELD_NUMBER: _ClassVar[int]
    TAKERS_TRADE_PRICE_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    IS_TAKER_API_USER_FIELD_NUMBER: _ClassVar[int]
    BURNING_MAN_SELECTION_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    offer_id: str
    pub_key_ring: PubKeyRing
    takers_trade_price: int
    supported_capabilities: _containers.RepeatedScalarFieldContainer[int]
    uid: str
    is_taker_api_user: bool
    burning_man_selection_height: int
    def __init__(self, offer_id: _Optional[str] = ..., pub_key_ring: _Optional[_Union[PubKeyRing, _Mapping]] = ..., takers_trade_price: _Optional[int] = ..., supported_capabilities: _Optional[_Iterable[int]] = ..., uid: _Optional[str] = ..., is_taker_api_user: bool = ..., burning_man_selection_height: _Optional[int] = ...) -> None: ...

class OfferAvailabilityResponse(_message.Message):
    __slots__ = ("offer_id", "availability_result", "supported_capabilities", "uid", "arbitrator", "mediator", "refund_agent")
    OFFER_ID_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_RESULT_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    ARBITRATOR_FIELD_NUMBER: _ClassVar[int]
    MEDIATOR_FIELD_NUMBER: _ClassVar[int]
    REFUND_AGENT_FIELD_NUMBER: _ClassVar[int]
    offer_id: str
    availability_result: AvailabilityResult
    supported_capabilities: _containers.RepeatedScalarFieldContainer[int]
    uid: str
    arbitrator: NodeAddress
    mediator: NodeAddress
    refund_agent: NodeAddress
    def __init__(self, offer_id: _Optional[str] = ..., availability_result: _Optional[_Union[AvailabilityResult, str]] = ..., supported_capabilities: _Optional[_Iterable[int]] = ..., uid: _Optional[str] = ..., arbitrator: _Optional[_Union[NodeAddress, _Mapping]] = ..., mediator: _Optional[_Union[NodeAddress, _Mapping]] = ..., refund_agent: _Optional[_Union[NodeAddress, _Mapping]] = ...) -> None: ...

class RefreshOfferMessage(_message.Message):
    __slots__ = ("hash_of_data_and_seq_nr", "signature", "hash_of_payload", "sequence_number")
    HASH_OF_DATA_AND_SEQ_NR_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    HASH_OF_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    hash_of_data_and_seq_nr: bytes
    signature: bytes
    hash_of_payload: bytes
    sequence_number: int
    def __init__(self, hash_of_data_and_seq_nr: _Optional[bytes] = ..., signature: _Optional[bytes] = ..., hash_of_payload: _Optional[bytes] = ..., sequence_number: _Optional[int] = ...) -> None: ...

class AddDataMessage(_message.Message):
    __slots__ = ("entry",)
    ENTRY_FIELD_NUMBER: _ClassVar[int]
    entry: StorageEntryWrapper
    def __init__(self, entry: _Optional[_Union[StorageEntryWrapper, _Mapping]] = ...) -> None: ...

class RemoveDataMessage(_message.Message):
    __slots__ = ("protected_storage_entry",)
    PROTECTED_STORAGE_ENTRY_FIELD_NUMBER: _ClassVar[int]
    protected_storage_entry: ProtectedStorageEntry
    def __init__(self, protected_storage_entry: _Optional[_Union[ProtectedStorageEntry, _Mapping]] = ...) -> None: ...

class RemoveMailboxDataMessage(_message.Message):
    __slots__ = ("protected_storage_entry",)
    PROTECTED_STORAGE_ENTRY_FIELD_NUMBER: _ClassVar[int]
    protected_storage_entry: ProtectedMailboxStorageEntry
    def __init__(self, protected_storage_entry: _Optional[_Union[ProtectedMailboxStorageEntry, _Mapping]] = ...) -> None: ...

class AddPersistableNetworkPayloadMessage(_message.Message):
    __slots__ = ("payload",)
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: PersistableNetworkPayload
    def __init__(self, payload: _Optional[_Union[PersistableNetworkPayload, _Mapping]] = ...) -> None: ...

class CloseConnectionMessage(_message.Message):
    __slots__ = ("reason",)
    REASON_FIELD_NUMBER: _ClassVar[int]
    reason: str
    def __init__(self, reason: _Optional[str] = ...) -> None: ...

class AckMessage(_message.Message):
    __slots__ = ("uid", "sender_node_address", "source_type", "source_msg_class_name", "source_uid", "source_id", "success", "error_message")
    UID_FIELD_NUMBER: _ClassVar[int]
    SENDER_NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_MSG_CLASS_NAME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_UID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    uid: str
    sender_node_address: NodeAddress
    source_type: str
    source_msg_class_name: str
    source_uid: str
    source_id: str
    success: bool
    error_message: str
    def __init__(self, uid: _Optional[str] = ..., sender_node_address: _Optional[_Union[NodeAddress, _Mapping]] = ..., source_type: _Optional[str] = ..., source_msg_class_name: _Optional[str] = ..., source_uid: _Optional[str] = ..., source_id: _Optional[str] = ..., success: bool = ..., error_message: _Optional[str] = ...) -> None: ...

class PrefixedSealedAndSignedMessage(_message.Message):
    __slots__ = ("node_address", "sealed_and_signed", "address_prefix_hash", "uid")
    NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    SEALED_AND_SIGNED_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_PREFIX_HASH_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    node_address: NodeAddress
    sealed_and_signed: SealedAndSigned
    address_prefix_hash: bytes
    uid: str
    def __init__(self, node_address: _Optional[_Union[NodeAddress, _Mapping]] = ..., sealed_and_signed: _Optional[_Union[SealedAndSigned, _Mapping]] = ..., address_prefix_hash: _Optional[bytes] = ..., uid: _Optional[str] = ...) -> None: ...

class InputsForDepositTxRequest(_message.Message):
    __slots__ = ("trade_id", "sender_node_address", "trade_amount", "trade_price", "tx_fee", "taker_fee", "is_currency_for_taker_fee_btc", "raw_transaction_inputs", "change_output_value", "change_output_address", "taker_multi_sig_pub_key", "taker_payout_address_string", "taker_pub_key_ring", "taker_payment_account_payload", "taker_account_id", "taker_fee_tx_id", "accepted_arbitrator_node_addresses", "accepted_mediator_node_addresses", "arbitrator_node_address", "mediator_node_address", "uid", "account_age_witness_signature_of_offer_id", "current_date", "accepted_refund_agent_node_addresses", "refund_agent_node_address", "hash_of_takers_payment_account_payload", "takers_payout_method_id", "burning_man_selection_height")
    TRADE_ID_FIELD_NUMBER: _ClassVar[int]
    SENDER_NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    TRADE_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    TRADE_PRICE_FIELD_NUMBER: _ClassVar[int]
    TX_FEE_FIELD_NUMBER: _ClassVar[int]
    TAKER_FEE_FIELD_NUMBER: _ClassVar[int]
    IS_CURRENCY_FOR_TAKER_FEE_BTC_FIELD_NUMBER: _ClassVar[int]
    RAW_TRANSACTION_INPUTS_FIELD_NUMBER: _ClassVar[int]
    CHANGE_OUTPUT_VALUE_FIELD_NUMBER: _ClassVar[int]
    CHANGE_OUTPUT_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    TAKER_MULTI_SIG_PUB_KEY_FIELD_NUMBER: _ClassVar[int]
    TAKER_PAYOUT_ADDRESS_STRING_FIELD_NUMBER: _ClassVar[int]
    TAKER_PUB_KEY_RING_FIELD_NUMBER: _ClassVar[int]
    TAKER_PAYMENT_ACCOUNT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    TAKER_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    TAKER_FEE_TX_ID_FIELD_NUMBER: _ClassVar[int]
    ACCEPTED_ARBITRATOR_NODE_ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    ACCEPTED_MEDIATOR_NODE_ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    ARBITRATOR_NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    MEDIATOR_NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_AGE_WITNESS_SIGNATURE_OF_OFFER_ID_FIELD_NUMBER: _ClassVar[int]
    CURRENT_DATE_FIELD_NUMBER: _ClassVar[int]
    ACCEPTED_REFUND_AGENT_NODE_ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    REFUND_AGENT_NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    HASH_OF_TAKERS_PAYMENT_ACCOUNT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    TAKERS_PAYOUT_METHOD_ID_FIELD_NUMBER: _ClassVar[int]
    BURNING_MAN_SELECTION_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    trade_id: str
    sender_node_address: NodeAddress
    trade_amount: int
    trade_price: int
    tx_fee: int
    taker_fee: int
    is_currency_for_taker_fee_btc: bool
    raw_transaction_inputs: _containers.RepeatedCompositeFieldContainer[RawTransactionInput]
    change_output_value: int
    change_output_address: str
    taker_multi_sig_pub_key: bytes
    taker_payout_address_string: str
    taker_pub_key_ring: PubKeyRing
    taker_payment_account_payload: PaymentAccountPayload
    taker_account_id: str
    taker_fee_tx_id: str
    accepted_arbitrator_node_addresses: _containers.RepeatedCompositeFieldContainer[NodeAddress]
    accepted_mediator_node_addresses: _containers.RepeatedCompositeFieldContainer[NodeAddress]
    arbitrator_node_address: NodeAddress
    mediator_node_address: NodeAddress
    uid: str
    account_age_witness_signature_of_offer_id: bytes
    current_date: int
    accepted_refund_agent_node_addresses: _containers.RepeatedCompositeFieldContainer[NodeAddress]
    refund_agent_node_address: NodeAddress
    hash_of_takers_payment_account_payload: bytes
    takers_payout_method_id: str
    burning_man_selection_height: int
    def __init__(self, trade_id: _Optional[str] = ..., sender_node_address: _Optional[_Union[NodeAddress, _Mapping]] = ..., trade_amount: _Optional[int] = ..., trade_price: _Optional[int] = ..., tx_fee: _Optional[int] = ..., taker_fee: _Optional[int] = ..., is_currency_for_taker_fee_btc: bool = ..., raw_transaction_inputs: _Optional[_Iterable[_Union[RawTransactionInput, _Mapping]]] = ..., change_output_value: _Optional[int] = ..., change_output_address: _Optional[str] = ..., taker_multi_sig_pub_key: _Optional[bytes] = ..., taker_payout_address_string: _Optional[str] = ..., taker_pub_key_ring: _Optional[_Union[PubKeyRing, _Mapping]] = ..., taker_payment_account_payload: _Optional[_Union[PaymentAccountPayload, _Mapping]] = ..., taker_account_id: _Optional[str] = ..., taker_fee_tx_id: _Optional[str] = ..., accepted_arbitrator_node_addresses: _Optional[_Iterable[_Union[NodeAddress, _Mapping]]] = ..., accepted_mediator_node_addresses: _Optional[_Iterable[_Union[NodeAddress, _Mapping]]] = ..., arbitrator_node_address: _Optional[_Union[NodeAddress, _Mapping]] = ..., mediator_node_address: _Optional[_Union[NodeAddress, _Mapping]] = ..., uid: _Optional[str] = ..., account_age_witness_signature_of_offer_id: _Optional[bytes] = ..., current_date: _Optional[int] = ..., accepted_refund_agent_node_addresses: _Optional[_Iterable[_Union[NodeAddress, _Mapping]]] = ..., refund_agent_node_address: _Optional[_Union[NodeAddress, _Mapping]] = ..., hash_of_takers_payment_account_payload: _Optional[bytes] = ..., takers_payout_method_id: _Optional[str] = ..., burning_man_selection_height: _Optional[int] = ...) -> None: ...

class InputsForDepositTxResponse(_message.Message):
    __slots__ = ("trade_id", "maker_payment_account_payload", "maker_account_id", "maker_contract_as_json", "maker_contract_signature", "maker_payout_address_string", "prepared_deposit_tx", "maker_inputs", "maker_multi_sig_pub_key", "sender_node_address", "uid", "account_age_witness_signature_of_prepared_deposit_tx", "current_date", "lock_time", "hash_of_makers_payment_account_payload", "makers_payout_method_id")
    TRADE_ID_FIELD_NUMBER: _ClassVar[int]
    MAKER_PAYMENT_ACCOUNT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    MAKER_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    MAKER_CONTRACT_AS_JSON_FIELD_NUMBER: _ClassVar[int]
    MAKER_CONTRACT_SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    MAKER_PAYOUT_ADDRESS_STRING_FIELD_NUMBER: _ClassVar[int]
    PREPARED_DEPOSIT_TX_FIELD_NUMBER: _ClassVar[int]
    MAKER_INPUTS_FIELD_NUMBER: _ClassVar[int]
    MAKER_MULTI_SIG_PUB_KEY_FIELD_NUMBER: _ClassVar[int]
    SENDER_NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_AGE_WITNESS_SIGNATURE_OF_PREPARED_DEPOSIT_TX_FIELD_NUMBER: _ClassVar[int]
    CURRENT_DATE_FIELD_NUMBER: _ClassVar[int]
    LOCK_TIME_FIELD_NUMBER: _ClassVar[int]
    HASH_OF_MAKERS_PAYMENT_ACCOUNT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    MAKERS_PAYOUT_METHOD_ID_FIELD_NUMBER: _ClassVar[int]
    trade_id: str
    maker_payment_account_payload: PaymentAccountPayload
    maker_account_id: str
    maker_contract_as_json: str
    maker_contract_signature: str
    maker_payout_address_string: str
    prepared_deposit_tx: bytes
    maker_inputs: _containers.RepeatedCompositeFieldContainer[RawTransactionInput]
    maker_multi_sig_pub_key: bytes
    sender_node_address: NodeAddress
    uid: str
    account_age_witness_signature_of_prepared_deposit_tx: bytes
    current_date: int
    lock_time: int
    hash_of_makers_payment_account_payload: bytes
    makers_payout_method_id: str
    def __init__(self, trade_id: _Optional[str] = ..., maker_payment_account_payload: _Optional[_Union[PaymentAccountPayload, _Mapping]] = ..., maker_account_id: _Optional[str] = ..., maker_contract_as_json: _Optional[str] = ..., maker_contract_signature: _Optional[str] = ..., maker_payout_address_string: _Optional[str] = ..., prepared_deposit_tx: _Optional[bytes] = ..., maker_inputs: _Optional[_Iterable[_Union[RawTransactionInput, _Mapping]]] = ..., maker_multi_sig_pub_key: _Optional[bytes] = ..., sender_node_address: _Optional[_Union[NodeAddress, _Mapping]] = ..., uid: _Optional[str] = ..., account_age_witness_signature_of_prepared_deposit_tx: _Optional[bytes] = ..., current_date: _Optional[int] = ..., lock_time: _Optional[int] = ..., hash_of_makers_payment_account_payload: _Optional[bytes] = ..., makers_payout_method_id: _Optional[str] = ...) -> None: ...

class DelayedPayoutTxSignatureRequest(_message.Message):
    __slots__ = ("uid", "trade_id", "sender_node_address", "delayed_payout_tx", "delayed_payout_tx_seller_signature")
    UID_FIELD_NUMBER: _ClassVar[int]
    TRADE_ID_FIELD_NUMBER: _ClassVar[int]
    SENDER_NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    DELAYED_PAYOUT_TX_FIELD_NUMBER: _ClassVar[int]
    DELAYED_PAYOUT_TX_SELLER_SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    uid: str
    trade_id: str
    sender_node_address: NodeAddress
    delayed_payout_tx: bytes
    delayed_payout_tx_seller_signature: bytes
    def __init__(self, uid: _Optional[str] = ..., trade_id: _Optional[str] = ..., sender_node_address: _Optional[_Union[NodeAddress, _Mapping]] = ..., delayed_payout_tx: _Optional[bytes] = ..., delayed_payout_tx_seller_signature: _Optional[bytes] = ...) -> None: ...

class DelayedPayoutTxSignatureResponse(_message.Message):
    __slots__ = ("uid", "trade_id", "sender_node_address", "delayed_payout_tx_buyer_signature", "deposit_tx")
    UID_FIELD_NUMBER: _ClassVar[int]
    TRADE_ID_FIELD_NUMBER: _ClassVar[int]
    SENDER_NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    DELAYED_PAYOUT_TX_BUYER_SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    DEPOSIT_TX_FIELD_NUMBER: _ClassVar[int]
    uid: str
    trade_id: str
    sender_node_address: NodeAddress
    delayed_payout_tx_buyer_signature: bytes
    deposit_tx: bytes
    def __init__(self, uid: _Optional[str] = ..., trade_id: _Optional[str] = ..., sender_node_address: _Optional[_Union[NodeAddress, _Mapping]] = ..., delayed_payout_tx_buyer_signature: _Optional[bytes] = ..., deposit_tx: _Optional[bytes] = ...) -> None: ...

class DepositTxAndDelayedPayoutTxMessage(_message.Message):
    __slots__ = ("uid", "trade_id", "sender_node_address", "deposit_tx", "delayed_payout_tx", "seller_payment_account_payload")
    UID_FIELD_NUMBER: _ClassVar[int]
    TRADE_ID_FIELD_NUMBER: _ClassVar[int]
    SENDER_NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    DEPOSIT_TX_FIELD_NUMBER: _ClassVar[int]
    DELAYED_PAYOUT_TX_FIELD_NUMBER: _ClassVar[int]
    SELLER_PAYMENT_ACCOUNT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    uid: str
    trade_id: str
    sender_node_address: NodeAddress
    deposit_tx: bytes
    delayed_payout_tx: bytes
    seller_payment_account_payload: PaymentAccountPayload
    def __init__(self, uid: _Optional[str] = ..., trade_id: _Optional[str] = ..., sender_node_address: _Optional[_Union[NodeAddress, _Mapping]] = ..., deposit_tx: _Optional[bytes] = ..., delayed_payout_tx: _Optional[bytes] = ..., seller_payment_account_payload: _Optional[_Union[PaymentAccountPayload, _Mapping]] = ...) -> None: ...

class ShareBuyerPaymentAccountMessage(_message.Message):
    __slots__ = ("uid", "trade_id", "sender_node_address", "buyer_payment_account_payload")
    UID_FIELD_NUMBER: _ClassVar[int]
    TRADE_ID_FIELD_NUMBER: _ClassVar[int]
    SENDER_NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    BUYER_PAYMENT_ACCOUNT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    uid: str
    trade_id: str
    sender_node_address: NodeAddress
    buyer_payment_account_payload: PaymentAccountPayload
    def __init__(self, uid: _Optional[str] = ..., trade_id: _Optional[str] = ..., sender_node_address: _Optional[_Union[NodeAddress, _Mapping]] = ..., buyer_payment_account_payload: _Optional[_Union[PaymentAccountPayload, _Mapping]] = ...) -> None: ...

class DepositTxMessage(_message.Message):
    __slots__ = ("uid", "trade_id", "sender_node_address", "deposit_tx_without_witnesses")
    UID_FIELD_NUMBER: _ClassVar[int]
    TRADE_ID_FIELD_NUMBER: _ClassVar[int]
    SENDER_NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    DEPOSIT_TX_WITHOUT_WITNESSES_FIELD_NUMBER: _ClassVar[int]
    uid: str
    trade_id: str
    sender_node_address: NodeAddress
    deposit_tx_without_witnesses: bytes
    def __init__(self, uid: _Optional[str] = ..., trade_id: _Optional[str] = ..., sender_node_address: _Optional[_Union[NodeAddress, _Mapping]] = ..., deposit_tx_without_witnesses: _Optional[bytes] = ...) -> None: ...

class PeerPublishedDelayedPayoutTxMessage(_message.Message):
    __slots__ = ("uid", "trade_id", "sender_node_address")
    UID_FIELD_NUMBER: _ClassVar[int]
    TRADE_ID_FIELD_NUMBER: _ClassVar[int]
    SENDER_NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    uid: str
    trade_id: str
    sender_node_address: NodeAddress
    def __init__(self, uid: _Optional[str] = ..., trade_id: _Optional[str] = ..., sender_node_address: _Optional[_Union[NodeAddress, _Mapping]] = ...) -> None: ...

class CounterCurrencyTransferStartedMessage(_message.Message):
    __slots__ = ("trade_id", "buyer_payout_address", "sender_node_address", "buyer_signature", "counter_currency_tx_id", "uid", "counter_currency_extra_data")
    TRADE_ID_FIELD_NUMBER: _ClassVar[int]
    BUYER_PAYOUT_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    SENDER_NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    BUYER_SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    COUNTER_CURRENCY_TX_ID_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    COUNTER_CURRENCY_EXTRA_DATA_FIELD_NUMBER: _ClassVar[int]
    trade_id: str
    buyer_payout_address: str
    sender_node_address: NodeAddress
    buyer_signature: bytes
    counter_currency_tx_id: str
    uid: str
    counter_currency_extra_data: str
    def __init__(self, trade_id: _Optional[str] = ..., buyer_payout_address: _Optional[str] = ..., sender_node_address: _Optional[_Union[NodeAddress, _Mapping]] = ..., buyer_signature: _Optional[bytes] = ..., counter_currency_tx_id: _Optional[str] = ..., uid: _Optional[str] = ..., counter_currency_extra_data: _Optional[str] = ...) -> None: ...

class FinalizePayoutTxRequest(_message.Message):
    __slots__ = ("trade_id", "seller_signature", "seller_payout_address", "sender_node_address", "uid")
    TRADE_ID_FIELD_NUMBER: _ClassVar[int]
    SELLER_SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    SELLER_PAYOUT_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    SENDER_NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    trade_id: str
    seller_signature: bytes
    seller_payout_address: str
    sender_node_address: NodeAddress
    uid: str
    def __init__(self, trade_id: _Optional[str] = ..., seller_signature: _Optional[bytes] = ..., seller_payout_address: _Optional[str] = ..., sender_node_address: _Optional[_Union[NodeAddress, _Mapping]] = ..., uid: _Optional[str] = ...) -> None: ...

class PayoutTxPublishedMessage(_message.Message):
    __slots__ = ("trade_id", "payout_tx", "sender_node_address", "uid", "signed_witness")
    TRADE_ID_FIELD_NUMBER: _ClassVar[int]
    PAYOUT_TX_FIELD_NUMBER: _ClassVar[int]
    SENDER_NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    SIGNED_WITNESS_FIELD_NUMBER: _ClassVar[int]
    trade_id: str
    payout_tx: bytes
    sender_node_address: NodeAddress
    uid: str
    signed_witness: SignedWitness
    def __init__(self, trade_id: _Optional[str] = ..., payout_tx: _Optional[bytes] = ..., sender_node_address: _Optional[_Union[NodeAddress, _Mapping]] = ..., uid: _Optional[str] = ..., signed_witness: _Optional[_Union[SignedWitness, _Mapping]] = ...) -> None: ...

class MediatedPayoutTxPublishedMessage(_message.Message):
    __slots__ = ("trade_id", "payout_tx", "sender_node_address", "uid")
    TRADE_ID_FIELD_NUMBER: _ClassVar[int]
    PAYOUT_TX_FIELD_NUMBER: _ClassVar[int]
    SENDER_NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    trade_id: str
    payout_tx: bytes
    sender_node_address: NodeAddress
    uid: str
    def __init__(self, trade_id: _Optional[str] = ..., payout_tx: _Optional[bytes] = ..., sender_node_address: _Optional[_Union[NodeAddress, _Mapping]] = ..., uid: _Optional[str] = ...) -> None: ...

class MediatedPayoutTxSignatureMessage(_message.Message):
    __slots__ = ("uid", "trade_id", "tx_signature", "sender_node_address")
    UID_FIELD_NUMBER: _ClassVar[int]
    TRADE_ID_FIELD_NUMBER: _ClassVar[int]
    TX_SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    SENDER_NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    uid: str
    trade_id: str
    tx_signature: bytes
    sender_node_address: NodeAddress
    def __init__(self, uid: _Optional[str] = ..., trade_id: _Optional[str] = ..., tx_signature: _Optional[bytes] = ..., sender_node_address: _Optional[_Union[NodeAddress, _Mapping]] = ...) -> None: ...

class RefreshTradeStateRequest(_message.Message):
    __slots__ = ("uid", "trade_id", "sender_node_address")
    UID_FIELD_NUMBER: _ClassVar[int]
    TRADE_ID_FIELD_NUMBER: _ClassVar[int]
    SENDER_NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    uid: str
    trade_id: str
    sender_node_address: NodeAddress
    def __init__(self, uid: _Optional[str] = ..., trade_id: _Optional[str] = ..., sender_node_address: _Optional[_Union[NodeAddress, _Mapping]] = ...) -> None: ...

class TraderSignedWitnessMessage(_message.Message):
    __slots__ = ("uid", "trade_id", "sender_node_address", "signed_witness")
    UID_FIELD_NUMBER: _ClassVar[int]
    TRADE_ID_FIELD_NUMBER: _ClassVar[int]
    SENDER_NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    SIGNED_WITNESS_FIELD_NUMBER: _ClassVar[int]
    uid: str
    trade_id: str
    sender_node_address: NodeAddress
    signed_witness: SignedWitness
    def __init__(self, uid: _Optional[str] = ..., trade_id: _Optional[str] = ..., sender_node_address: _Optional[_Union[NodeAddress, _Mapping]] = ..., signed_witness: _Optional[_Union[SignedWitness, _Mapping]] = ...) -> None: ...

class SellersBsqSwapRequest(_message.Message):
    __slots__ = ("uid", "trade_id", "sender_node_address", "taker_pub_key_ring", "trade_amount", "tx_fee_per_vbyte", "maker_fee", "taker_fee", "trade_date")
    UID_FIELD_NUMBER: _ClassVar[int]
    TRADE_ID_FIELD_NUMBER: _ClassVar[int]
    SENDER_NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    TAKER_PUB_KEY_RING_FIELD_NUMBER: _ClassVar[int]
    TRADE_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    TX_FEE_PER_VBYTE_FIELD_NUMBER: _ClassVar[int]
    MAKER_FEE_FIELD_NUMBER: _ClassVar[int]
    TAKER_FEE_FIELD_NUMBER: _ClassVar[int]
    TRADE_DATE_FIELD_NUMBER: _ClassVar[int]
    uid: str
    trade_id: str
    sender_node_address: NodeAddress
    taker_pub_key_ring: PubKeyRing
    trade_amount: int
    tx_fee_per_vbyte: int
    maker_fee: int
    taker_fee: int
    trade_date: int
    def __init__(self, uid: _Optional[str] = ..., trade_id: _Optional[str] = ..., sender_node_address: _Optional[_Union[NodeAddress, _Mapping]] = ..., taker_pub_key_ring: _Optional[_Union[PubKeyRing, _Mapping]] = ..., trade_amount: _Optional[int] = ..., tx_fee_per_vbyte: _Optional[int] = ..., maker_fee: _Optional[int] = ..., taker_fee: _Optional[int] = ..., trade_date: _Optional[int] = ...) -> None: ...

class BuyersBsqSwapRequest(_message.Message):
    __slots__ = ("uid", "trade_id", "sender_node_address", "taker_pub_key_ring", "trade_amount", "tx_fee_per_vbyte", "maker_fee", "taker_fee", "trade_date", "bsq_inputs", "bsq_change", "buyers_btc_payout_address", "buyers_bsq_change_address")
    UID_FIELD_NUMBER: _ClassVar[int]
    TRADE_ID_FIELD_NUMBER: _ClassVar[int]
    SENDER_NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    TAKER_PUB_KEY_RING_FIELD_NUMBER: _ClassVar[int]
    TRADE_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    TX_FEE_PER_VBYTE_FIELD_NUMBER: _ClassVar[int]
    MAKER_FEE_FIELD_NUMBER: _ClassVar[int]
    TAKER_FEE_FIELD_NUMBER: _ClassVar[int]
    TRADE_DATE_FIELD_NUMBER: _ClassVar[int]
    BSQ_INPUTS_FIELD_NUMBER: _ClassVar[int]
    BSQ_CHANGE_FIELD_NUMBER: _ClassVar[int]
    BUYERS_BTC_PAYOUT_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    BUYERS_BSQ_CHANGE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    uid: str
    trade_id: str
    sender_node_address: NodeAddress
    taker_pub_key_ring: PubKeyRing
    trade_amount: int
    tx_fee_per_vbyte: int
    maker_fee: int
    taker_fee: int
    trade_date: int
    bsq_inputs: _containers.RepeatedCompositeFieldContainer[RawTransactionInput]
    bsq_change: int
    buyers_btc_payout_address: str
    buyers_bsq_change_address: str
    def __init__(self, uid: _Optional[str] = ..., trade_id: _Optional[str] = ..., sender_node_address: _Optional[_Union[NodeAddress, _Mapping]] = ..., taker_pub_key_ring: _Optional[_Union[PubKeyRing, _Mapping]] = ..., trade_amount: _Optional[int] = ..., tx_fee_per_vbyte: _Optional[int] = ..., maker_fee: _Optional[int] = ..., taker_fee: _Optional[int] = ..., trade_date: _Optional[int] = ..., bsq_inputs: _Optional[_Iterable[_Union[RawTransactionInput, _Mapping]]] = ..., bsq_change: _Optional[int] = ..., buyers_btc_payout_address: _Optional[str] = ..., buyers_bsq_change_address: _Optional[str] = ...) -> None: ...

class BsqSwapTxInputsMessage(_message.Message):
    __slots__ = ("uid", "trade_id", "sender_node_address", "bsq_inputs", "bsq_change", "buyers_btc_payout_address", "buyers_bsq_change_address")
    UID_FIELD_NUMBER: _ClassVar[int]
    TRADE_ID_FIELD_NUMBER: _ClassVar[int]
    SENDER_NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    BSQ_INPUTS_FIELD_NUMBER: _ClassVar[int]
    BSQ_CHANGE_FIELD_NUMBER: _ClassVar[int]
    BUYERS_BTC_PAYOUT_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    BUYERS_BSQ_CHANGE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    uid: str
    trade_id: str
    sender_node_address: NodeAddress
    bsq_inputs: _containers.RepeatedCompositeFieldContainer[RawTransactionInput]
    bsq_change: int
    buyers_btc_payout_address: str
    buyers_bsq_change_address: str
    def __init__(self, uid: _Optional[str] = ..., trade_id: _Optional[str] = ..., sender_node_address: _Optional[_Union[NodeAddress, _Mapping]] = ..., bsq_inputs: _Optional[_Iterable[_Union[RawTransactionInput, _Mapping]]] = ..., bsq_change: _Optional[int] = ..., buyers_btc_payout_address: _Optional[str] = ..., buyers_bsq_change_address: _Optional[str] = ...) -> None: ...

class BsqSwapFinalizeTxRequest(_message.Message):
    __slots__ = ("uid", "trade_id", "sender_node_address", "tx", "btc_inputs", "btc_change", "bsq_payout_address", "btc_change_address")
    UID_FIELD_NUMBER: _ClassVar[int]
    TRADE_ID_FIELD_NUMBER: _ClassVar[int]
    SENDER_NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    TX_FIELD_NUMBER: _ClassVar[int]
    BTC_INPUTS_FIELD_NUMBER: _ClassVar[int]
    BTC_CHANGE_FIELD_NUMBER: _ClassVar[int]
    BSQ_PAYOUT_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    BTC_CHANGE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    uid: str
    trade_id: str
    sender_node_address: NodeAddress
    tx: bytes
    btc_inputs: _containers.RepeatedCompositeFieldContainer[RawTransactionInput]
    btc_change: int
    bsq_payout_address: str
    btc_change_address: str
    def __init__(self, uid: _Optional[str] = ..., trade_id: _Optional[str] = ..., sender_node_address: _Optional[_Union[NodeAddress, _Mapping]] = ..., tx: _Optional[bytes] = ..., btc_inputs: _Optional[_Iterable[_Union[RawTransactionInput, _Mapping]]] = ..., btc_change: _Optional[int] = ..., bsq_payout_address: _Optional[str] = ..., btc_change_address: _Optional[str] = ...) -> None: ...

class BsqSwapFinalizedTxMessage(_message.Message):
    __slots__ = ("uid", "trade_id", "sender_node_address", "tx")
    UID_FIELD_NUMBER: _ClassVar[int]
    TRADE_ID_FIELD_NUMBER: _ClassVar[int]
    SENDER_NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    TX_FIELD_NUMBER: _ClassVar[int]
    uid: str
    trade_id: str
    sender_node_address: NodeAddress
    tx: bytes
    def __init__(self, uid: _Optional[str] = ..., trade_id: _Optional[str] = ..., sender_node_address: _Optional[_Union[NodeAddress, _Mapping]] = ..., tx: _Optional[bytes] = ...) -> None: ...

class OpenNewDisputeMessage(_message.Message):
    __slots__ = ("dispute", "sender_node_address", "uid", "type")
    DISPUTE_FIELD_NUMBER: _ClassVar[int]
    SENDER_NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    dispute: Dispute
    sender_node_address: NodeAddress
    uid: str
    type: SupportType
    def __init__(self, dispute: _Optional[_Union[Dispute, _Mapping]] = ..., sender_node_address: _Optional[_Union[NodeAddress, _Mapping]] = ..., uid: _Optional[str] = ..., type: _Optional[_Union[SupportType, str]] = ...) -> None: ...

class PeerOpenedDisputeMessage(_message.Message):
    __slots__ = ("dispute", "sender_node_address", "uid", "type")
    DISPUTE_FIELD_NUMBER: _ClassVar[int]
    SENDER_NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    dispute: Dispute
    sender_node_address: NodeAddress
    uid: str
    type: SupportType
    def __init__(self, dispute: _Optional[_Union[Dispute, _Mapping]] = ..., sender_node_address: _Optional[_Union[NodeAddress, _Mapping]] = ..., uid: _Optional[str] = ..., type: _Optional[_Union[SupportType, str]] = ...) -> None: ...

class ChatMessage(_message.Message):
    __slots__ = ("date", "trade_id", "trader_id", "sender_is_trader", "message", "attachments", "arrived", "stored_in_mailbox", "is_system_message", "sender_node_address", "uid", "send_message_error", "acknowledged", "ack_error", "type", "was_displayed")
    DATE_FIELD_NUMBER: _ClassVar[int]
    TRADE_ID_FIELD_NUMBER: _ClassVar[int]
    TRADER_ID_FIELD_NUMBER: _ClassVar[int]
    SENDER_IS_TRADER_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENTS_FIELD_NUMBER: _ClassVar[int]
    ARRIVED_FIELD_NUMBER: _ClassVar[int]
    STORED_IN_MAILBOX_FIELD_NUMBER: _ClassVar[int]
    IS_SYSTEM_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SENDER_NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    SEND_MESSAGE_ERROR_FIELD_NUMBER: _ClassVar[int]
    ACKNOWLEDGED_FIELD_NUMBER: _ClassVar[int]
    ACK_ERROR_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    WAS_DISPLAYED_FIELD_NUMBER: _ClassVar[int]
    date: int
    trade_id: str
    trader_id: int
    sender_is_trader: bool
    message: str
    attachments: _containers.RepeatedCompositeFieldContainer[Attachment]
    arrived: bool
    stored_in_mailbox: bool
    is_system_message: bool
    sender_node_address: NodeAddress
    uid: str
    send_message_error: str
    acknowledged: bool
    ack_error: str
    type: SupportType
    was_displayed: bool
    def __init__(self, date: _Optional[int] = ..., trade_id: _Optional[str] = ..., trader_id: _Optional[int] = ..., sender_is_trader: bool = ..., message: _Optional[str] = ..., attachments: _Optional[_Iterable[_Union[Attachment, _Mapping]]] = ..., arrived: bool = ..., stored_in_mailbox: bool = ..., is_system_message: bool = ..., sender_node_address: _Optional[_Union[NodeAddress, _Mapping]] = ..., uid: _Optional[str] = ..., send_message_error: _Optional[str] = ..., acknowledged: bool = ..., ack_error: _Optional[str] = ..., type: _Optional[_Union[SupportType, str]] = ..., was_displayed: bool = ...) -> None: ...

class DisputeResultMessage(_message.Message):
    __slots__ = ("uid", "dispute_result", "sender_node_address", "type")
    UID_FIELD_NUMBER: _ClassVar[int]
    DISPUTE_RESULT_FIELD_NUMBER: _ClassVar[int]
    SENDER_NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    uid: str
    dispute_result: DisputeResult
    sender_node_address: NodeAddress
    type: SupportType
    def __init__(self, uid: _Optional[str] = ..., dispute_result: _Optional[_Union[DisputeResult, _Mapping]] = ..., sender_node_address: _Optional[_Union[NodeAddress, _Mapping]] = ..., type: _Optional[_Union[SupportType, str]] = ...) -> None: ...

class PeerPublishedDisputePayoutTxMessage(_message.Message):
    __slots__ = ("uid", "transaction", "trade_id", "sender_node_address", "type")
    UID_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    TRADE_ID_FIELD_NUMBER: _ClassVar[int]
    SENDER_NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    uid: str
    transaction: bytes
    trade_id: str
    sender_node_address: NodeAddress
    type: SupportType
    def __init__(self, uid: _Optional[str] = ..., transaction: _Optional[bytes] = ..., trade_id: _Optional[str] = ..., sender_node_address: _Optional[_Union[NodeAddress, _Mapping]] = ..., type: _Optional[_Union[SupportType, str]] = ...) -> None: ...

class PrivateNotificationMessage(_message.Message):
    __slots__ = ("uid", "sender_node_address", "private_notification_payload")
    UID_FIELD_NUMBER: _ClassVar[int]
    SENDER_NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_NOTIFICATION_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    uid: str
    sender_node_address: NodeAddress
    private_notification_payload: PrivateNotificationPayload
    def __init__(self, uid: _Optional[str] = ..., sender_node_address: _Optional[_Union[NodeAddress, _Mapping]] = ..., private_notification_payload: _Optional[_Union[PrivateNotificationPayload, _Mapping]] = ...) -> None: ...

class GetBlocksRequest(_message.Message):
    __slots__ = ("from_block_height", "nonce", "sender_node_address", "supported_capabilities")
    FROM_BLOCK_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    NONCE_FIELD_NUMBER: _ClassVar[int]
    SENDER_NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    from_block_height: int
    nonce: int
    sender_node_address: NodeAddress
    supported_capabilities: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, from_block_height: _Optional[int] = ..., nonce: _Optional[int] = ..., sender_node_address: _Optional[_Union[NodeAddress, _Mapping]] = ..., supported_capabilities: _Optional[_Iterable[int]] = ...) -> None: ...

class GetBlocksResponse(_message.Message):
    __slots__ = ("raw_blocks", "request_nonce")
    RAW_BLOCKS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_NONCE_FIELD_NUMBER: _ClassVar[int]
    raw_blocks: _containers.RepeatedCompositeFieldContainer[BaseBlock]
    request_nonce: int
    def __init__(self, raw_blocks: _Optional[_Iterable[_Union[BaseBlock, _Mapping]]] = ..., request_nonce: _Optional[int] = ...) -> None: ...

class NewBlockBroadcastMessage(_message.Message):
    __slots__ = ("raw_block",)
    RAW_BLOCK_FIELD_NUMBER: _ClassVar[int]
    raw_block: BaseBlock
    def __init__(self, raw_block: _Optional[_Union[BaseBlock, _Mapping]] = ...) -> None: ...

class RepublishGovernanceDataRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class NewDaoStateHashMessage(_message.Message):
    __slots__ = ("state_hash",)
    STATE_HASH_FIELD_NUMBER: _ClassVar[int]
    state_hash: DaoStateHash
    def __init__(self, state_hash: _Optional[_Union[DaoStateHash, _Mapping]] = ...) -> None: ...

class NewProposalStateHashMessage(_message.Message):
    __slots__ = ("state_hash",)
    STATE_HASH_FIELD_NUMBER: _ClassVar[int]
    state_hash: ProposalStateHash
    def __init__(self, state_hash: _Optional[_Union[ProposalStateHash, _Mapping]] = ...) -> None: ...

class NewBlindVoteStateHashMessage(_message.Message):
    __slots__ = ("state_hash",)
    STATE_HASH_FIELD_NUMBER: _ClassVar[int]
    state_hash: BlindVoteStateHash
    def __init__(self, state_hash: _Optional[_Union[BlindVoteStateHash, _Mapping]] = ...) -> None: ...

class GetDaoStateHashesRequest(_message.Message):
    __slots__ = ("height", "nonce")
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    NONCE_FIELD_NUMBER: _ClassVar[int]
    height: int
    nonce: int
    def __init__(self, height: _Optional[int] = ..., nonce: _Optional[int] = ...) -> None: ...

class GetProposalStateHashesRequest(_message.Message):
    __slots__ = ("height", "nonce")
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    NONCE_FIELD_NUMBER: _ClassVar[int]
    height: int
    nonce: int
    def __init__(self, height: _Optional[int] = ..., nonce: _Optional[int] = ...) -> None: ...

class GetBlindVoteStateHashesRequest(_message.Message):
    __slots__ = ("height", "nonce")
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    NONCE_FIELD_NUMBER: _ClassVar[int]
    height: int
    nonce: int
    def __init__(self, height: _Optional[int] = ..., nonce: _Optional[int] = ...) -> None: ...

class GetDaoStateHashesResponse(_message.Message):
    __slots__ = ("state_hashes", "request_nonce")
    STATE_HASHES_FIELD_NUMBER: _ClassVar[int]
    REQUEST_NONCE_FIELD_NUMBER: _ClassVar[int]
    state_hashes: _containers.RepeatedCompositeFieldContainer[DaoStateHash]
    request_nonce: int
    def __init__(self, state_hashes: _Optional[_Iterable[_Union[DaoStateHash, _Mapping]]] = ..., request_nonce: _Optional[int] = ...) -> None: ...

class GetProposalStateHashesResponse(_message.Message):
    __slots__ = ("state_hashes", "request_nonce")
    STATE_HASHES_FIELD_NUMBER: _ClassVar[int]
    REQUEST_NONCE_FIELD_NUMBER: _ClassVar[int]
    state_hashes: _containers.RepeatedCompositeFieldContainer[ProposalStateHash]
    request_nonce: int
    def __init__(self, state_hashes: _Optional[_Iterable[_Union[ProposalStateHash, _Mapping]]] = ..., request_nonce: _Optional[int] = ...) -> None: ...

class GetBlindVoteStateHashesResponse(_message.Message):
    __slots__ = ("state_hashes", "request_nonce")
    STATE_HASHES_FIELD_NUMBER: _ClassVar[int]
    REQUEST_NONCE_FIELD_NUMBER: _ClassVar[int]
    state_hashes: _containers.RepeatedCompositeFieldContainer[BlindVoteStateHash]
    request_nonce: int
    def __init__(self, state_hashes: _Optional[_Iterable[_Union[BlindVoteStateHash, _Mapping]]] = ..., request_nonce: _Optional[int] = ...) -> None: ...

class NodeAddress(_message.Message):
    __slots__ = ("host_name", "port")
    HOST_NAME_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    host_name: str
    port: int
    def __init__(self, host_name: _Optional[str] = ..., port: _Optional[int] = ...) -> None: ...

class Peer(_message.Message):
    __slots__ = ("node_address", "date", "supported_capabilities")
    NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    node_address: NodeAddress
    date: int
    supported_capabilities: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, node_address: _Optional[_Union[NodeAddress, _Mapping]] = ..., date: _Optional[int] = ..., supported_capabilities: _Optional[_Iterable[int]] = ...) -> None: ...

class PubKeyRing(_message.Message):
    __slots__ = ("signature_pub_key_bytes", "encryption_pub_key_bytes")
    SIGNATURE_PUB_KEY_BYTES_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_PUB_KEY_BYTES_FIELD_NUMBER: _ClassVar[int]
    signature_pub_key_bytes: bytes
    encryption_pub_key_bytes: bytes
    def __init__(self, signature_pub_key_bytes: _Optional[bytes] = ..., encryption_pub_key_bytes: _Optional[bytes] = ...) -> None: ...

class SealedAndSigned(_message.Message):
    __slots__ = ("encrypted_secret_key", "encrypted_payload_with_hmac", "signature", "sig_public_key_bytes")
    ENCRYPTED_SECRET_KEY_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_PAYLOAD_WITH_HMAC_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    SIG_PUBLIC_KEY_BYTES_FIELD_NUMBER: _ClassVar[int]
    encrypted_secret_key: bytes
    encrypted_payload_with_hmac: bytes
    signature: bytes
    sig_public_key_bytes: bytes
    def __init__(self, encrypted_secret_key: _Optional[bytes] = ..., encrypted_payload_with_hmac: _Optional[bytes] = ..., signature: _Optional[bytes] = ..., sig_public_key_bytes: _Optional[bytes] = ...) -> None: ...

class StoragePayload(_message.Message):
    __slots__ = ("alert", "arbitrator", "mediator", "filter", "mailbox_storage_payload", "offer_payload", "temp_proposal_payload", "refund_agent", "bsq_swap_offer_payload")
    ALERT_FIELD_NUMBER: _ClassVar[int]
    ARBITRATOR_FIELD_NUMBER: _ClassVar[int]
    MEDIATOR_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    MAILBOX_STORAGE_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    OFFER_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    TEMP_PROPOSAL_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    REFUND_AGENT_FIELD_NUMBER: _ClassVar[int]
    BSQ_SWAP_OFFER_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    alert: Alert
    arbitrator: Arbitrator
    mediator: Mediator
    filter: Filter
    mailbox_storage_payload: MailboxStoragePayload
    offer_payload: OfferPayload
    temp_proposal_payload: TempProposalPayload
    refund_agent: RefundAgent
    bsq_swap_offer_payload: BsqSwapOfferPayload
    def __init__(self, alert: _Optional[_Union[Alert, _Mapping]] = ..., arbitrator: _Optional[_Union[Arbitrator, _Mapping]] = ..., mediator: _Optional[_Union[Mediator, _Mapping]] = ..., filter: _Optional[_Union[Filter, _Mapping]] = ..., mailbox_storage_payload: _Optional[_Union[MailboxStoragePayload, _Mapping]] = ..., offer_payload: _Optional[_Union[OfferPayload, _Mapping]] = ..., temp_proposal_payload: _Optional[_Union[TempProposalPayload, _Mapping]] = ..., refund_agent: _Optional[_Union[RefundAgent, _Mapping]] = ..., bsq_swap_offer_payload: _Optional[_Union[BsqSwapOfferPayload, _Mapping]] = ...) -> None: ...

class PersistableNetworkPayload(_message.Message):
    __slots__ = ("account_age_witness", "trade_statistics2", "proposal_payload", "blind_vote_payload", "signed_witness", "trade_statistics3")
    ACCOUNT_AGE_WITNESS_FIELD_NUMBER: _ClassVar[int]
    TRADE_STATISTICS2_FIELD_NUMBER: _ClassVar[int]
    PROPOSAL_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    BLIND_VOTE_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    SIGNED_WITNESS_FIELD_NUMBER: _ClassVar[int]
    TRADE_STATISTICS3_FIELD_NUMBER: _ClassVar[int]
    account_age_witness: AccountAgeWitness
    trade_statistics2: TradeStatistics2
    proposal_payload: ProposalPayload
    blind_vote_payload: BlindVotePayload
    signed_witness: SignedWitness
    trade_statistics3: TradeStatistics3
    def __init__(self, account_age_witness: _Optional[_Union[AccountAgeWitness, _Mapping]] = ..., trade_statistics2: _Optional[_Union[TradeStatistics2, _Mapping]] = ..., proposal_payload: _Optional[_Union[ProposalPayload, _Mapping]] = ..., blind_vote_payload: _Optional[_Union[BlindVotePayload, _Mapping]] = ..., signed_witness: _Optional[_Union[SignedWitness, _Mapping]] = ..., trade_statistics3: _Optional[_Union[TradeStatistics3, _Mapping]] = ...) -> None: ...

class ProtectedStorageEntry(_message.Message):
    __slots__ = ("storagePayload", "owner_pub_key_bytes", "sequence_number", "signature", "creation_time_stamp")
    STORAGEPAYLOAD_FIELD_NUMBER: _ClassVar[int]
    OWNER_PUB_KEY_BYTES_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    CREATION_TIME_STAMP_FIELD_NUMBER: _ClassVar[int]
    storagePayload: StoragePayload
    owner_pub_key_bytes: bytes
    sequence_number: int
    signature: bytes
    creation_time_stamp: int
    def __init__(self, storagePayload: _Optional[_Union[StoragePayload, _Mapping]] = ..., owner_pub_key_bytes: _Optional[bytes] = ..., sequence_number: _Optional[int] = ..., signature: _Optional[bytes] = ..., creation_time_stamp: _Optional[int] = ...) -> None: ...

class StorageEntryWrapper(_message.Message):
    __slots__ = ("protected_storage_entry", "protected_mailbox_storage_entry")
    PROTECTED_STORAGE_ENTRY_FIELD_NUMBER: _ClassVar[int]
    PROTECTED_MAILBOX_STORAGE_ENTRY_FIELD_NUMBER: _ClassVar[int]
    protected_storage_entry: ProtectedStorageEntry
    protected_mailbox_storage_entry: ProtectedMailboxStorageEntry
    def __init__(self, protected_storage_entry: _Optional[_Union[ProtectedStorageEntry, _Mapping]] = ..., protected_mailbox_storage_entry: _Optional[_Union[ProtectedMailboxStorageEntry, _Mapping]] = ...) -> None: ...

class ProtectedMailboxStorageEntry(_message.Message):
    __slots__ = ("entry", "receivers_pub_key_bytes")
    ENTRY_FIELD_NUMBER: _ClassVar[int]
    RECEIVERS_PUB_KEY_BYTES_FIELD_NUMBER: _ClassVar[int]
    entry: ProtectedStorageEntry
    receivers_pub_key_bytes: bytes
    def __init__(self, entry: _Optional[_Union[ProtectedStorageEntry, _Mapping]] = ..., receivers_pub_key_bytes: _Optional[bytes] = ...) -> None: ...

class DataAndSeqNrPair(_message.Message):
    __slots__ = ("payload", "sequence_number")
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    payload: StoragePayload
    sequence_number: int
    def __init__(self, payload: _Optional[_Union[StoragePayload, _Mapping]] = ..., sequence_number: _Optional[int] = ...) -> None: ...

class MailboxMessageList(_message.Message):
    __slots__ = ("mailbox_item",)
    MAILBOX_ITEM_FIELD_NUMBER: _ClassVar[int]
    mailbox_item: _containers.RepeatedCompositeFieldContainer[MailboxItem]
    def __init__(self, mailbox_item: _Optional[_Iterable[_Union[MailboxItem, _Mapping]]] = ...) -> None: ...

class RemovedPayloadsMap(_message.Message):
    __slots__ = ("date_by_hashes",)
    class DateByHashesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    DATE_BY_HASHES_FIELD_NUMBER: _ClassVar[int]
    date_by_hashes: _containers.ScalarMap[str, int]
    def __init__(self, date_by_hashes: _Optional[_Mapping[str, int]] = ...) -> None: ...

class IgnoredMailboxMap(_message.Message):
    __slots__ = ("data",)
    class DataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: _containers.ScalarMap[str, int]
    def __init__(self, data: _Optional[_Mapping[str, int]] = ...) -> None: ...

class MailboxItem(_message.Message):
    __slots__ = ("protected_mailbox_storage_entry", "decrypted_message_with_pub_key")
    PROTECTED_MAILBOX_STORAGE_ENTRY_FIELD_NUMBER: _ClassVar[int]
    DECRYPTED_MESSAGE_WITH_PUB_KEY_FIELD_NUMBER: _ClassVar[int]
    protected_mailbox_storage_entry: ProtectedMailboxStorageEntry
    decrypted_message_with_pub_key: DecryptedMessageWithPubKey
    def __init__(self, protected_mailbox_storage_entry: _Optional[_Union[ProtectedMailboxStorageEntry, _Mapping]] = ..., decrypted_message_with_pub_key: _Optional[_Union[DecryptedMessageWithPubKey, _Mapping]] = ...) -> None: ...

class DecryptedMessageWithPubKey(_message.Message):
    __slots__ = ("network_envelope", "signature_pub_key_bytes")
    NETWORK_ENVELOPE_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_PUB_KEY_BYTES_FIELD_NUMBER: _ClassVar[int]
    network_envelope: NetworkEnvelope
    signature_pub_key_bytes: bytes
    def __init__(self, network_envelope: _Optional[_Union[NetworkEnvelope, _Mapping]] = ..., signature_pub_key_bytes: _Optional[bytes] = ...) -> None: ...

class PrivateNotificationPayload(_message.Message):
    __slots__ = ("message", "signature_as_base64", "sig_public_key_bytes")
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_AS_BASE64_FIELD_NUMBER: _ClassVar[int]
    SIG_PUBLIC_KEY_BYTES_FIELD_NUMBER: _ClassVar[int]
    message: str
    signature_as_base64: str
    sig_public_key_bytes: bytes
    def __init__(self, message: _Optional[str] = ..., signature_as_base64: _Optional[str] = ..., sig_public_key_bytes: _Optional[bytes] = ...) -> None: ...

class PaymentAccountFilter(_message.Message):
    __slots__ = ("payment_method_id", "get_method_name", "value")
    PAYMENT_METHOD_ID_FIELD_NUMBER: _ClassVar[int]
    GET_METHOD_NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    payment_method_id: str
    get_method_name: str
    value: str
    def __init__(self, payment_method_id: _Optional[str] = ..., get_method_name: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class Alert(_message.Message):
    __slots__ = ("message", "version", "is_update_info", "signature_as_base64", "owner_pub_key_bytes", "extra_data", "is_pre_release_info")
    class ExtraDataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    IS_UPDATE_INFO_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_AS_BASE64_FIELD_NUMBER: _ClassVar[int]
    OWNER_PUB_KEY_BYTES_FIELD_NUMBER: _ClassVar[int]
    EXTRA_DATA_FIELD_NUMBER: _ClassVar[int]
    IS_PRE_RELEASE_INFO_FIELD_NUMBER: _ClassVar[int]
    message: str
    version: str
    is_update_info: bool
    signature_as_base64: str
    owner_pub_key_bytes: bytes
    extra_data: _containers.ScalarMap[str, str]
    is_pre_release_info: bool
    def __init__(self, message: _Optional[str] = ..., version: _Optional[str] = ..., is_update_info: bool = ..., signature_as_base64: _Optional[str] = ..., owner_pub_key_bytes: _Optional[bytes] = ..., extra_data: _Optional[_Mapping[str, str]] = ..., is_pre_release_info: bool = ...) -> None: ...

class Arbitrator(_message.Message):
    __slots__ = ("node_address", "language_codes", "registration_date", "registration_signature", "registration_pub_key", "pub_key_ring", "btc_pub_key", "btc_address", "email_address", "info", "extra_data")
    class ExtraDataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODES_FIELD_NUMBER: _ClassVar[int]
    REGISTRATION_DATE_FIELD_NUMBER: _ClassVar[int]
    REGISTRATION_SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    REGISTRATION_PUB_KEY_FIELD_NUMBER: _ClassVar[int]
    PUB_KEY_RING_FIELD_NUMBER: _ClassVar[int]
    BTC_PUB_KEY_FIELD_NUMBER: _ClassVar[int]
    BTC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    EMAIL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    EXTRA_DATA_FIELD_NUMBER: _ClassVar[int]
    node_address: NodeAddress
    language_codes: _containers.RepeatedScalarFieldContainer[str]
    registration_date: int
    registration_signature: str
    registration_pub_key: bytes
    pub_key_ring: PubKeyRing
    btc_pub_key: bytes
    btc_address: str
    email_address: str
    info: str
    extra_data: _containers.ScalarMap[str, str]
    def __init__(self, node_address: _Optional[_Union[NodeAddress, _Mapping]] = ..., language_codes: _Optional[_Iterable[str]] = ..., registration_date: _Optional[int] = ..., registration_signature: _Optional[str] = ..., registration_pub_key: _Optional[bytes] = ..., pub_key_ring: _Optional[_Union[PubKeyRing, _Mapping]] = ..., btc_pub_key: _Optional[bytes] = ..., btc_address: _Optional[str] = ..., email_address: _Optional[str] = ..., info: _Optional[str] = ..., extra_data: _Optional[_Mapping[str, str]] = ...) -> None: ...

class Mediator(_message.Message):
    __slots__ = ("node_address", "language_codes", "registration_date", "registration_signature", "registration_pub_key", "pub_key_ring", "email_address", "info", "extra_data")
    class ExtraDataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODES_FIELD_NUMBER: _ClassVar[int]
    REGISTRATION_DATE_FIELD_NUMBER: _ClassVar[int]
    REGISTRATION_SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    REGISTRATION_PUB_KEY_FIELD_NUMBER: _ClassVar[int]
    PUB_KEY_RING_FIELD_NUMBER: _ClassVar[int]
    EMAIL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    EXTRA_DATA_FIELD_NUMBER: _ClassVar[int]
    node_address: NodeAddress
    language_codes: _containers.RepeatedScalarFieldContainer[str]
    registration_date: int
    registration_signature: str
    registration_pub_key: bytes
    pub_key_ring: PubKeyRing
    email_address: str
    info: str
    extra_data: _containers.ScalarMap[str, str]
    def __init__(self, node_address: _Optional[_Union[NodeAddress, _Mapping]] = ..., language_codes: _Optional[_Iterable[str]] = ..., registration_date: _Optional[int] = ..., registration_signature: _Optional[str] = ..., registration_pub_key: _Optional[bytes] = ..., pub_key_ring: _Optional[_Union[PubKeyRing, _Mapping]] = ..., email_address: _Optional[str] = ..., info: _Optional[str] = ..., extra_data: _Optional[_Mapping[str, str]] = ...) -> None: ...

class RefundAgent(_message.Message):
    __slots__ = ("node_address", "language_codes", "registration_date", "registration_signature", "registration_pub_key", "pub_key_ring", "email_address", "info", "extra_data")
    class ExtraDataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODES_FIELD_NUMBER: _ClassVar[int]
    REGISTRATION_DATE_FIELD_NUMBER: _ClassVar[int]
    REGISTRATION_SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    REGISTRATION_PUB_KEY_FIELD_NUMBER: _ClassVar[int]
    PUB_KEY_RING_FIELD_NUMBER: _ClassVar[int]
    EMAIL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    EXTRA_DATA_FIELD_NUMBER: _ClassVar[int]
    node_address: NodeAddress
    language_codes: _containers.RepeatedScalarFieldContainer[str]
    registration_date: int
    registration_signature: str
    registration_pub_key: bytes
    pub_key_ring: PubKeyRing
    email_address: str
    info: str
    extra_data: _containers.ScalarMap[str, str]
    def __init__(self, node_address: _Optional[_Union[NodeAddress, _Mapping]] = ..., language_codes: _Optional[_Iterable[str]] = ..., registration_date: _Optional[int] = ..., registration_signature: _Optional[str] = ..., registration_pub_key: _Optional[bytes] = ..., pub_key_ring: _Optional[_Union[PubKeyRing, _Mapping]] = ..., email_address: _Optional[str] = ..., info: _Optional[str] = ..., extra_data: _Optional[_Mapping[str, str]] = ...) -> None: ...

class Filter(_message.Message):
    __slots__ = ("node_addresses_banned_from_trading", "banned_offer_ids", "banned_payment_accounts", "signature_as_base64", "owner_pub_key_bytes", "extra_data", "banned_currencies", "banned_payment_methods", "arbitrators", "seed_nodes", "price_relay_nodes", "prevent_public_btc_network", "btc_nodes", "disable_dao", "disable_dao_below_version", "disable_trade_below_version", "mediators", "refundAgents", "bannedSignerPubKeys", "btc_fee_receiver_addresses", "creation_date", "signer_pub_key_as_hex", "bannedPrivilegedDevPubKeys", "disable_auto_conf", "banned_auto_conf_explorers", "node_addresses_banned_from_network", "disable_api", "disable_mempool_validation", "disable_pow_message", "pow_difficulty", "maker_fee_btc", "taker_fee_btc", "maker_fee_bsq", "taker_fee_bsq", "enabled_pow_versions", "delayedPayoutPaymentAccounts", "addedBtcNodes", "addedSeedNodes", "uid")
    class ExtraDataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NODE_ADDRESSES_BANNED_FROM_TRADING_FIELD_NUMBER: _ClassVar[int]
    BANNED_OFFER_IDS_FIELD_NUMBER: _ClassVar[int]
    BANNED_PAYMENT_ACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_AS_BASE64_FIELD_NUMBER: _ClassVar[int]
    OWNER_PUB_KEY_BYTES_FIELD_NUMBER: _ClassVar[int]
    EXTRA_DATA_FIELD_NUMBER: _ClassVar[int]
    BANNED_CURRENCIES_FIELD_NUMBER: _ClassVar[int]
    BANNED_PAYMENT_METHODS_FIELD_NUMBER: _ClassVar[int]
    ARBITRATORS_FIELD_NUMBER: _ClassVar[int]
    SEED_NODES_FIELD_NUMBER: _ClassVar[int]
    PRICE_RELAY_NODES_FIELD_NUMBER: _ClassVar[int]
    PREVENT_PUBLIC_BTC_NETWORK_FIELD_NUMBER: _ClassVar[int]
    BTC_NODES_FIELD_NUMBER: _ClassVar[int]
    DISABLE_DAO_FIELD_NUMBER: _ClassVar[int]
    DISABLE_DAO_BELOW_VERSION_FIELD_NUMBER: _ClassVar[int]
    DISABLE_TRADE_BELOW_VERSION_FIELD_NUMBER: _ClassVar[int]
    MEDIATORS_FIELD_NUMBER: _ClassVar[int]
    REFUNDAGENTS_FIELD_NUMBER: _ClassVar[int]
    BANNEDSIGNERPUBKEYS_FIELD_NUMBER: _ClassVar[int]
    BTC_FEE_RECEIVER_ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    CREATION_DATE_FIELD_NUMBER: _ClassVar[int]
    SIGNER_PUB_KEY_AS_HEX_FIELD_NUMBER: _ClassVar[int]
    BANNEDPRIVILEGEDDEVPUBKEYS_FIELD_NUMBER: _ClassVar[int]
    DISABLE_AUTO_CONF_FIELD_NUMBER: _ClassVar[int]
    BANNED_AUTO_CONF_EXPLORERS_FIELD_NUMBER: _ClassVar[int]
    NODE_ADDRESSES_BANNED_FROM_NETWORK_FIELD_NUMBER: _ClassVar[int]
    DISABLE_API_FIELD_NUMBER: _ClassVar[int]
    DISABLE_MEMPOOL_VALIDATION_FIELD_NUMBER: _ClassVar[int]
    DISABLE_POW_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    POW_DIFFICULTY_FIELD_NUMBER: _ClassVar[int]
    MAKER_FEE_BTC_FIELD_NUMBER: _ClassVar[int]
    TAKER_FEE_BTC_FIELD_NUMBER: _ClassVar[int]
    MAKER_FEE_BSQ_FIELD_NUMBER: _ClassVar[int]
    TAKER_FEE_BSQ_FIELD_NUMBER: _ClassVar[int]
    ENABLED_POW_VERSIONS_FIELD_NUMBER: _ClassVar[int]
    DELAYEDPAYOUTPAYMENTACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    ADDEDBTCNODES_FIELD_NUMBER: _ClassVar[int]
    ADDEDSEEDNODES_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    node_addresses_banned_from_trading: _containers.RepeatedScalarFieldContainer[str]
    banned_offer_ids: _containers.RepeatedScalarFieldContainer[str]
    banned_payment_accounts: _containers.RepeatedCompositeFieldContainer[PaymentAccountFilter]
    signature_as_base64: str
    owner_pub_key_bytes: bytes
    extra_data: _containers.ScalarMap[str, str]
    banned_currencies: _containers.RepeatedScalarFieldContainer[str]
    banned_payment_methods: _containers.RepeatedScalarFieldContainer[str]
    arbitrators: _containers.RepeatedScalarFieldContainer[str]
    seed_nodes: _containers.RepeatedScalarFieldContainer[str]
    price_relay_nodes: _containers.RepeatedScalarFieldContainer[str]
    prevent_public_btc_network: bool
    btc_nodes: _containers.RepeatedScalarFieldContainer[str]
    disable_dao: bool
    disable_dao_below_version: str
    disable_trade_below_version: str
    mediators: _containers.RepeatedScalarFieldContainer[str]
    refundAgents: _containers.RepeatedScalarFieldContainer[str]
    bannedSignerPubKeys: _containers.RepeatedScalarFieldContainer[str]
    btc_fee_receiver_addresses: _containers.RepeatedScalarFieldContainer[str]
    creation_date: int
    signer_pub_key_as_hex: str
    bannedPrivilegedDevPubKeys: _containers.RepeatedScalarFieldContainer[str]
    disable_auto_conf: bool
    banned_auto_conf_explorers: _containers.RepeatedScalarFieldContainer[str]
    node_addresses_banned_from_network: _containers.RepeatedScalarFieldContainer[str]
    disable_api: bool
    disable_mempool_validation: bool
    disable_pow_message: bool
    pow_difficulty: float
    maker_fee_btc: int
    taker_fee_btc: int
    maker_fee_bsq: int
    taker_fee_bsq: int
    enabled_pow_versions: _containers.RepeatedScalarFieldContainer[int]
    delayedPayoutPaymentAccounts: _containers.RepeatedCompositeFieldContainer[PaymentAccountFilter]
    addedBtcNodes: _containers.RepeatedScalarFieldContainer[str]
    addedSeedNodes: _containers.RepeatedScalarFieldContainer[str]
    uid: str
    def __init__(self, node_addresses_banned_from_trading: _Optional[_Iterable[str]] = ..., banned_offer_ids: _Optional[_Iterable[str]] = ..., banned_payment_accounts: _Optional[_Iterable[_Union[PaymentAccountFilter, _Mapping]]] = ..., signature_as_base64: _Optional[str] = ..., owner_pub_key_bytes: _Optional[bytes] = ..., extra_data: _Optional[_Mapping[str, str]] = ..., banned_currencies: _Optional[_Iterable[str]] = ..., banned_payment_methods: _Optional[_Iterable[str]] = ..., arbitrators: _Optional[_Iterable[str]] = ..., seed_nodes: _Optional[_Iterable[str]] = ..., price_relay_nodes: _Optional[_Iterable[str]] = ..., prevent_public_btc_network: bool = ..., btc_nodes: _Optional[_Iterable[str]] = ..., disable_dao: bool = ..., disable_dao_below_version: _Optional[str] = ..., disable_trade_below_version: _Optional[str] = ..., mediators: _Optional[_Iterable[str]] = ..., refundAgents: _Optional[_Iterable[str]] = ..., bannedSignerPubKeys: _Optional[_Iterable[str]] = ..., btc_fee_receiver_addresses: _Optional[_Iterable[str]] = ..., creation_date: _Optional[int] = ..., signer_pub_key_as_hex: _Optional[str] = ..., bannedPrivilegedDevPubKeys: _Optional[_Iterable[str]] = ..., disable_auto_conf: bool = ..., banned_auto_conf_explorers: _Optional[_Iterable[str]] = ..., node_addresses_banned_from_network: _Optional[_Iterable[str]] = ..., disable_api: bool = ..., disable_mempool_validation: bool = ..., disable_pow_message: bool = ..., pow_difficulty: _Optional[float] = ..., maker_fee_btc: _Optional[int] = ..., taker_fee_btc: _Optional[int] = ..., maker_fee_bsq: _Optional[int] = ..., taker_fee_bsq: _Optional[int] = ..., enabled_pow_versions: _Optional[_Iterable[int]] = ..., delayedPayoutPaymentAccounts: _Optional[_Iterable[_Union[PaymentAccountFilter, _Mapping]]] = ..., addedBtcNodes: _Optional[_Iterable[str]] = ..., addedSeedNodes: _Optional[_Iterable[str]] = ..., uid: _Optional[str] = ...) -> None: ...

class TradeStatistics2(_message.Message):
    __slots__ = ("base_currency", "counter_currency", "direction", "trade_price", "trade_amount", "trade_date", "payment_method_id", "offer_date", "offer_use_market_based_price", "offer_market_price_margin", "offer_amount", "offer_min_amount", "offer_id", "deposit_tx_id", "hash", "extra_data")
    class ExtraDataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    BASE_CURRENCY_FIELD_NUMBER: _ClassVar[int]
    COUNTER_CURRENCY_FIELD_NUMBER: _ClassVar[int]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    TRADE_PRICE_FIELD_NUMBER: _ClassVar[int]
    TRADE_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    TRADE_DATE_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_METHOD_ID_FIELD_NUMBER: _ClassVar[int]
    OFFER_DATE_FIELD_NUMBER: _ClassVar[int]
    OFFER_USE_MARKET_BASED_PRICE_FIELD_NUMBER: _ClassVar[int]
    OFFER_MARKET_PRICE_MARGIN_FIELD_NUMBER: _ClassVar[int]
    OFFER_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    OFFER_MIN_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    OFFER_ID_FIELD_NUMBER: _ClassVar[int]
    DEPOSIT_TX_ID_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    EXTRA_DATA_FIELD_NUMBER: _ClassVar[int]
    base_currency: str
    counter_currency: str
    direction: OfferDirection
    trade_price: int
    trade_amount: int
    trade_date: int
    payment_method_id: str
    offer_date: int
    offer_use_market_based_price: bool
    offer_market_price_margin: float
    offer_amount: int
    offer_min_amount: int
    offer_id: str
    deposit_tx_id: str
    hash: bytes
    extra_data: _containers.ScalarMap[str, str]
    def __init__(self, base_currency: _Optional[str] = ..., counter_currency: _Optional[str] = ..., direction: _Optional[_Union[OfferDirection, str]] = ..., trade_price: _Optional[int] = ..., trade_amount: _Optional[int] = ..., trade_date: _Optional[int] = ..., payment_method_id: _Optional[str] = ..., offer_date: _Optional[int] = ..., offer_use_market_based_price: bool = ..., offer_market_price_margin: _Optional[float] = ..., offer_amount: _Optional[int] = ..., offer_min_amount: _Optional[int] = ..., offer_id: _Optional[str] = ..., deposit_tx_id: _Optional[str] = ..., hash: _Optional[bytes] = ..., extra_data: _Optional[_Mapping[str, str]] = ...) -> None: ...

class TradeStatistics3(_message.Message):
    __slots__ = ("currency", "price", "amount", "payment_method", "date", "mediator", "refund_agent", "hash", "extra_data")
    class ExtraDataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_METHOD_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    MEDIATOR_FIELD_NUMBER: _ClassVar[int]
    REFUND_AGENT_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    EXTRA_DATA_FIELD_NUMBER: _ClassVar[int]
    currency: str
    price: int
    amount: int
    payment_method: str
    date: int
    mediator: str
    refund_agent: str
    hash: bytes
    extra_data: _containers.ScalarMap[str, str]
    def __init__(self, currency: _Optional[str] = ..., price: _Optional[int] = ..., amount: _Optional[int] = ..., payment_method: _Optional[str] = ..., date: _Optional[int] = ..., mediator: _Optional[str] = ..., refund_agent: _Optional[str] = ..., hash: _Optional[bytes] = ..., extra_data: _Optional[_Mapping[str, str]] = ...) -> None: ...

class MailboxStoragePayload(_message.Message):
    __slots__ = ("prefixed_sealed_and_signed_message", "sender_pub_key_for_add_operation_bytes", "owner_pub_key_bytes", "extra_data")
    class ExtraDataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    PREFIXED_SEALED_AND_SIGNED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SENDER_PUB_KEY_FOR_ADD_OPERATION_BYTES_FIELD_NUMBER: _ClassVar[int]
    OWNER_PUB_KEY_BYTES_FIELD_NUMBER: _ClassVar[int]
    EXTRA_DATA_FIELD_NUMBER: _ClassVar[int]
    prefixed_sealed_and_signed_message: PrefixedSealedAndSignedMessage
    sender_pub_key_for_add_operation_bytes: bytes
    owner_pub_key_bytes: bytes
    extra_data: _containers.ScalarMap[str, str]
    def __init__(self, prefixed_sealed_and_signed_message: _Optional[_Union[PrefixedSealedAndSignedMessage, _Mapping]] = ..., sender_pub_key_for_add_operation_bytes: _Optional[bytes] = ..., owner_pub_key_bytes: _Optional[bytes] = ..., extra_data: _Optional[_Mapping[str, str]] = ...) -> None: ...

class OfferPayload(_message.Message):
    __slots__ = ("id", "date", "owner_node_address", "pub_key_ring", "direction", "price", "market_price_margin", "use_market_based_price", "amount", "min_amount", "base_currency_code", "counter_currency_code", "arbitrator_node_addresses", "mediator_node_addresses", "payment_method_id", "maker_payment_account_id", "offer_fee_payment_tx_id", "country_code", "accepted_country_codes", "bank_id", "accepted_bank_ids", "version_nr", "block_height_at_offer_creation", "tx_fee", "maker_fee", "is_currency_for_maker_fee_btc", "buyer_security_deposit", "seller_security_deposit", "max_trade_limit", "max_trade_period", "use_auto_close", "use_re_open_after_auto_close", "lower_close_price", "upper_close_price", "is_private_offer", "hash_of_challenge", "extra_data", "protocol_version")
    class ExtraDataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    OWNER_NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PUB_KEY_RING_FIELD_NUMBER: _ClassVar[int]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    MARKET_PRICE_MARGIN_FIELD_NUMBER: _ClassVar[int]
    USE_MARKET_BASED_PRICE_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    MIN_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    BASE_CURRENCY_CODE_FIELD_NUMBER: _ClassVar[int]
    COUNTER_CURRENCY_CODE_FIELD_NUMBER: _ClassVar[int]
    ARBITRATOR_NODE_ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    MEDIATOR_NODE_ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_METHOD_ID_FIELD_NUMBER: _ClassVar[int]
    MAKER_PAYMENT_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    OFFER_FEE_PAYMENT_TX_ID_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    ACCEPTED_COUNTRY_CODES_FIELD_NUMBER: _ClassVar[int]
    BANK_ID_FIELD_NUMBER: _ClassVar[int]
    ACCEPTED_BANK_IDS_FIELD_NUMBER: _ClassVar[int]
    VERSION_NR_FIELD_NUMBER: _ClassVar[int]
    BLOCK_HEIGHT_AT_OFFER_CREATION_FIELD_NUMBER: _ClassVar[int]
    TX_FEE_FIELD_NUMBER: _ClassVar[int]
    MAKER_FEE_FIELD_NUMBER: _ClassVar[int]
    IS_CURRENCY_FOR_MAKER_FEE_BTC_FIELD_NUMBER: _ClassVar[int]
    BUYER_SECURITY_DEPOSIT_FIELD_NUMBER: _ClassVar[int]
    SELLER_SECURITY_DEPOSIT_FIELD_NUMBER: _ClassVar[int]
    MAX_TRADE_LIMIT_FIELD_NUMBER: _ClassVar[int]
    MAX_TRADE_PERIOD_FIELD_NUMBER: _ClassVar[int]
    USE_AUTO_CLOSE_FIELD_NUMBER: _ClassVar[int]
    USE_RE_OPEN_AFTER_AUTO_CLOSE_FIELD_NUMBER: _ClassVar[int]
    LOWER_CLOSE_PRICE_FIELD_NUMBER: _ClassVar[int]
    UPPER_CLOSE_PRICE_FIELD_NUMBER: _ClassVar[int]
    IS_PRIVATE_OFFER_FIELD_NUMBER: _ClassVar[int]
    HASH_OF_CHALLENGE_FIELD_NUMBER: _ClassVar[int]
    EXTRA_DATA_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_VERSION_FIELD_NUMBER: _ClassVar[int]
    id: str
    date: int
    owner_node_address: NodeAddress
    pub_key_ring: PubKeyRing
    direction: OfferDirection
    price: int
    market_price_margin: float
    use_market_based_price: bool
    amount: int
    min_amount: int
    base_currency_code: str
    counter_currency_code: str
    arbitrator_node_addresses: _containers.RepeatedCompositeFieldContainer[NodeAddress]
    mediator_node_addresses: _containers.RepeatedCompositeFieldContainer[NodeAddress]
    payment_method_id: str
    maker_payment_account_id: str
    offer_fee_payment_tx_id: str
    country_code: str
    accepted_country_codes: _containers.RepeatedScalarFieldContainer[str]
    bank_id: str
    accepted_bank_ids: _containers.RepeatedScalarFieldContainer[str]
    version_nr: str
    block_height_at_offer_creation: int
    tx_fee: int
    maker_fee: int
    is_currency_for_maker_fee_btc: bool
    buyer_security_deposit: int
    seller_security_deposit: int
    max_trade_limit: int
    max_trade_period: int
    use_auto_close: bool
    use_re_open_after_auto_close: bool
    lower_close_price: int
    upper_close_price: int
    is_private_offer: bool
    hash_of_challenge: str
    extra_data: _containers.ScalarMap[str, str]
    protocol_version: int
    def __init__(self, id: _Optional[str] = ..., date: _Optional[int] = ..., owner_node_address: _Optional[_Union[NodeAddress, _Mapping]] = ..., pub_key_ring: _Optional[_Union[PubKeyRing, _Mapping]] = ..., direction: _Optional[_Union[OfferDirection, str]] = ..., price: _Optional[int] = ..., market_price_margin: _Optional[float] = ..., use_market_based_price: bool = ..., amount: _Optional[int] = ..., min_amount: _Optional[int] = ..., base_currency_code: _Optional[str] = ..., counter_currency_code: _Optional[str] = ..., arbitrator_node_addresses: _Optional[_Iterable[_Union[NodeAddress, _Mapping]]] = ..., mediator_node_addresses: _Optional[_Iterable[_Union[NodeAddress, _Mapping]]] = ..., payment_method_id: _Optional[str] = ..., maker_payment_account_id: _Optional[str] = ..., offer_fee_payment_tx_id: _Optional[str] = ..., country_code: _Optional[str] = ..., accepted_country_codes: _Optional[_Iterable[str]] = ..., bank_id: _Optional[str] = ..., accepted_bank_ids: _Optional[_Iterable[str]] = ..., version_nr: _Optional[str] = ..., block_height_at_offer_creation: _Optional[int] = ..., tx_fee: _Optional[int] = ..., maker_fee: _Optional[int] = ..., is_currency_for_maker_fee_btc: bool = ..., buyer_security_deposit: _Optional[int] = ..., seller_security_deposit: _Optional[int] = ..., max_trade_limit: _Optional[int] = ..., max_trade_period: _Optional[int] = ..., use_auto_close: bool = ..., use_re_open_after_auto_close: bool = ..., lower_close_price: _Optional[int] = ..., upper_close_price: _Optional[int] = ..., is_private_offer: bool = ..., hash_of_challenge: _Optional[str] = ..., extra_data: _Optional[_Mapping[str, str]] = ..., protocol_version: _Optional[int] = ...) -> None: ...

class BsqSwapOfferPayload(_message.Message):
    __slots__ = ("id", "date", "owner_node_address", "pub_key_ring", "direction", "price", "amount", "min_amount", "proof_of_work", "extra_data", "version_nr", "protocol_version")
    class ExtraDataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    OWNER_NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PUB_KEY_RING_FIELD_NUMBER: _ClassVar[int]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    MIN_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    PROOF_OF_WORK_FIELD_NUMBER: _ClassVar[int]
    EXTRA_DATA_FIELD_NUMBER: _ClassVar[int]
    VERSION_NR_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_VERSION_FIELD_NUMBER: _ClassVar[int]
    id: str
    date: int
    owner_node_address: NodeAddress
    pub_key_ring: PubKeyRing
    direction: OfferDirection
    price: int
    amount: int
    min_amount: int
    proof_of_work: ProofOfWork
    extra_data: _containers.ScalarMap[str, str]
    version_nr: str
    protocol_version: int
    def __init__(self, id: _Optional[str] = ..., date: _Optional[int] = ..., owner_node_address: _Optional[_Union[NodeAddress, _Mapping]] = ..., pub_key_ring: _Optional[_Union[PubKeyRing, _Mapping]] = ..., direction: _Optional[_Union[OfferDirection, str]] = ..., price: _Optional[int] = ..., amount: _Optional[int] = ..., min_amount: _Optional[int] = ..., proof_of_work: _Optional[_Union[ProofOfWork, _Mapping]] = ..., extra_data: _Optional[_Mapping[str, str]] = ..., version_nr: _Optional[str] = ..., protocol_version: _Optional[int] = ...) -> None: ...

class ProofOfWork(_message.Message):
    __slots__ = ("payload", "counter", "challenge", "difficulty", "duration", "solution", "version")
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    COUNTER_FIELD_NUMBER: _ClassVar[int]
    CHALLENGE_FIELD_NUMBER: _ClassVar[int]
    DIFFICULTY_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    SOLUTION_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    payload: bytes
    counter: int
    challenge: bytes
    difficulty: float
    duration: int
    solution: bytes
    version: int
    def __init__(self, payload: _Optional[bytes] = ..., counter: _Optional[int] = ..., challenge: _Optional[bytes] = ..., difficulty: _Optional[float] = ..., duration: _Optional[int] = ..., solution: _Optional[bytes] = ..., version: _Optional[int] = ...) -> None: ...

class AccountAgeWitness(_message.Message):
    __slots__ = ("hash", "date")
    HASH_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    hash: bytes
    date: int
    def __init__(self, hash: _Optional[bytes] = ..., date: _Optional[int] = ...) -> None: ...

class SignedWitness(_message.Message):
    __slots__ = ("verification_method", "account_age_witness_hash", "signature", "signer_pub_key", "witness_owner_pub_key", "date", "trade_amount")
    class VerificationMethod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PB_ERROR: _ClassVar[SignedWitness.VerificationMethod]
        ARBITRATOR: _ClassVar[SignedWitness.VerificationMethod]
        TRADE: _ClassVar[SignedWitness.VerificationMethod]
    PB_ERROR: SignedWitness.VerificationMethod
    ARBITRATOR: SignedWitness.VerificationMethod
    TRADE: SignedWitness.VerificationMethod
    VERIFICATION_METHOD_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_AGE_WITNESS_HASH_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    SIGNER_PUB_KEY_FIELD_NUMBER: _ClassVar[int]
    WITNESS_OWNER_PUB_KEY_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    TRADE_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    verification_method: SignedWitness.VerificationMethod
    account_age_witness_hash: bytes
    signature: bytes
    signer_pub_key: bytes
    witness_owner_pub_key: bytes
    date: int
    trade_amount: int
    def __init__(self, verification_method: _Optional[_Union[SignedWitness.VerificationMethod, str]] = ..., account_age_witness_hash: _Optional[bytes] = ..., signature: _Optional[bytes] = ..., signer_pub_key: _Optional[bytes] = ..., witness_owner_pub_key: _Optional[bytes] = ..., date: _Optional[int] = ..., trade_amount: _Optional[int] = ...) -> None: ...

class Dispute(_message.Message):
    __slots__ = ("trade_id", "id", "trader_id", "dispute_opener_is_buyer", "dispute_opener_is_maker", "opening_date", "trader_pub_key_ring", "trade_date", "contract", "contract_hash", "deposit_tx_serialized", "payout_tx_serialized", "deposit_tx_id", "payout_tx_id", "contract_as_json", "maker_contract_signature", "taker_contract_signature", "agent_pub_key_ring", "is_support_ticket", "chat_message", "is_closed", "dispute_result", "dispute_payout_tx_id", "support_type", "mediators_dispute_result", "delayed_payout_tx_id", "donation_address_of_delayed_payout_tx", "state", "trade_period_end", "extra_data", "burning_man_selection_height", "trade_tx_fee")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NEEDS_UPGRADE: _ClassVar[Dispute.State]
        NEW: _ClassVar[Dispute.State]
        OPEN: _ClassVar[Dispute.State]
        REOPENED: _ClassVar[Dispute.State]
        CLOSED: _ClassVar[Dispute.State]
        RESULT_PROPOSED: _ClassVar[Dispute.State]
    NEEDS_UPGRADE: Dispute.State
    NEW: Dispute.State
    OPEN: Dispute.State
    REOPENED: Dispute.State
    CLOSED: Dispute.State
    RESULT_PROPOSED: Dispute.State
    class ExtraDataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    TRADE_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    TRADER_ID_FIELD_NUMBER: _ClassVar[int]
    DISPUTE_OPENER_IS_BUYER_FIELD_NUMBER: _ClassVar[int]
    DISPUTE_OPENER_IS_MAKER_FIELD_NUMBER: _ClassVar[int]
    OPENING_DATE_FIELD_NUMBER: _ClassVar[int]
    TRADER_PUB_KEY_RING_FIELD_NUMBER: _ClassVar[int]
    TRADE_DATE_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_HASH_FIELD_NUMBER: _ClassVar[int]
    DEPOSIT_TX_SERIALIZED_FIELD_NUMBER: _ClassVar[int]
    PAYOUT_TX_SERIALIZED_FIELD_NUMBER: _ClassVar[int]
    DEPOSIT_TX_ID_FIELD_NUMBER: _ClassVar[int]
    PAYOUT_TX_ID_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_AS_JSON_FIELD_NUMBER: _ClassVar[int]
    MAKER_CONTRACT_SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    TAKER_CONTRACT_SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    AGENT_PUB_KEY_RING_FIELD_NUMBER: _ClassVar[int]
    IS_SUPPORT_TICKET_FIELD_NUMBER: _ClassVar[int]
    CHAT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    IS_CLOSED_FIELD_NUMBER: _ClassVar[int]
    DISPUTE_RESULT_FIELD_NUMBER: _ClassVar[int]
    DISPUTE_PAYOUT_TX_ID_FIELD_NUMBER: _ClassVar[int]
    SUPPORT_TYPE_FIELD_NUMBER: _ClassVar[int]
    MEDIATORS_DISPUTE_RESULT_FIELD_NUMBER: _ClassVar[int]
    DELAYED_PAYOUT_TX_ID_FIELD_NUMBER: _ClassVar[int]
    DONATION_ADDRESS_OF_DELAYED_PAYOUT_TX_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    TRADE_PERIOD_END_FIELD_NUMBER: _ClassVar[int]
    EXTRA_DATA_FIELD_NUMBER: _ClassVar[int]
    BURNING_MAN_SELECTION_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    TRADE_TX_FEE_FIELD_NUMBER: _ClassVar[int]
    trade_id: str
    id: str
    trader_id: int
    dispute_opener_is_buyer: bool
    dispute_opener_is_maker: bool
    opening_date: int
    trader_pub_key_ring: PubKeyRing
    trade_date: int
    contract: Contract
    contract_hash: bytes
    deposit_tx_serialized: bytes
    payout_tx_serialized: bytes
    deposit_tx_id: str
    payout_tx_id: str
    contract_as_json: str
    maker_contract_signature: str
    taker_contract_signature: str
    agent_pub_key_ring: PubKeyRing
    is_support_ticket: bool
    chat_message: _containers.RepeatedCompositeFieldContainer[ChatMessage]
    is_closed: bool
    dispute_result: DisputeResult
    dispute_payout_tx_id: str
    support_type: SupportType
    mediators_dispute_result: str
    delayed_payout_tx_id: str
    donation_address_of_delayed_payout_tx: str
    state: Dispute.State
    trade_period_end: int
    extra_data: _containers.ScalarMap[str, str]
    burning_man_selection_height: int
    trade_tx_fee: int
    def __init__(self, trade_id: _Optional[str] = ..., id: _Optional[str] = ..., trader_id: _Optional[int] = ..., dispute_opener_is_buyer: bool = ..., dispute_opener_is_maker: bool = ..., opening_date: _Optional[int] = ..., trader_pub_key_ring: _Optional[_Union[PubKeyRing, _Mapping]] = ..., trade_date: _Optional[int] = ..., contract: _Optional[_Union[Contract, _Mapping]] = ..., contract_hash: _Optional[bytes] = ..., deposit_tx_serialized: _Optional[bytes] = ..., payout_tx_serialized: _Optional[bytes] = ..., deposit_tx_id: _Optional[str] = ..., payout_tx_id: _Optional[str] = ..., contract_as_json: _Optional[str] = ..., maker_contract_signature: _Optional[str] = ..., taker_contract_signature: _Optional[str] = ..., agent_pub_key_ring: _Optional[_Union[PubKeyRing, _Mapping]] = ..., is_support_ticket: bool = ..., chat_message: _Optional[_Iterable[_Union[ChatMessage, _Mapping]]] = ..., is_closed: bool = ..., dispute_result: _Optional[_Union[DisputeResult, _Mapping]] = ..., dispute_payout_tx_id: _Optional[str] = ..., support_type: _Optional[_Union[SupportType, str]] = ..., mediators_dispute_result: _Optional[str] = ..., delayed_payout_tx_id: _Optional[str] = ..., donation_address_of_delayed_payout_tx: _Optional[str] = ..., state: _Optional[_Union[Dispute.State, str]] = ..., trade_period_end: _Optional[int] = ..., extra_data: _Optional[_Mapping[str, str]] = ..., burning_man_selection_height: _Optional[int] = ..., trade_tx_fee: _Optional[int] = ...) -> None: ...

class Attachment(_message.Message):
    __slots__ = ("file_name", "bytes")
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    BYTES_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    bytes: bytes
    def __init__(self, file_name: _Optional[str] = ..., bytes: _Optional[bytes] = ...) -> None: ...

class DisputeResult(_message.Message):
    __slots__ = ("trade_id", "trader_id", "winner", "reason_ordinal", "tamper_proof_evidence", "id_verification", "screen_cast", "summary_notes", "chat_message", "arbitrator_signature", "buyer_payout_amount", "seller_payout_amount", "arbitrator_pub_key", "close_date", "is_loser_publisher", "payout_adjustment_percent", "payout_suggestion")
    class Winner(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PB_ERROR_WINNER: _ClassVar[DisputeResult.Winner]
        BUYER: _ClassVar[DisputeResult.Winner]
        SELLER: _ClassVar[DisputeResult.Winner]
    PB_ERROR_WINNER: DisputeResult.Winner
    BUYER: DisputeResult.Winner
    SELLER: DisputeResult.Winner
    class Reason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PB_ERROR_REASON: _ClassVar[DisputeResult.Reason]
        OTHER: _ClassVar[DisputeResult.Reason]
        BUG: _ClassVar[DisputeResult.Reason]
        USABILITY: _ClassVar[DisputeResult.Reason]
        SCAM: _ClassVar[DisputeResult.Reason]
        PROTOCOL_VIOLATION: _ClassVar[DisputeResult.Reason]
        NO_REPLY: _ClassVar[DisputeResult.Reason]
        BANK_PROBLEMS: _ClassVar[DisputeResult.Reason]
        OPTION_TRADE: _ClassVar[DisputeResult.Reason]
        SELLER_NOT_RESPONDING: _ClassVar[DisputeResult.Reason]
        WRONG_SENDER_ACCOUNT: _ClassVar[DisputeResult.Reason]
        TRADE_ALREADY_SETTLED: _ClassVar[DisputeResult.Reason]
        PEER_WAS_LATE: _ClassVar[DisputeResult.Reason]
    PB_ERROR_REASON: DisputeResult.Reason
    OTHER: DisputeResult.Reason
    BUG: DisputeResult.Reason
    USABILITY: DisputeResult.Reason
    SCAM: DisputeResult.Reason
    PROTOCOL_VIOLATION: DisputeResult.Reason
    NO_REPLY: DisputeResult.Reason
    BANK_PROBLEMS: DisputeResult.Reason
    OPTION_TRADE: DisputeResult.Reason
    SELLER_NOT_RESPONDING: DisputeResult.Reason
    WRONG_SENDER_ACCOUNT: DisputeResult.Reason
    TRADE_ALREADY_SETTLED: DisputeResult.Reason
    PEER_WAS_LATE: DisputeResult.Reason
    class PayoutSuggestion(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CUSTOM_PAYOUT: _ClassVar[DisputeResult.PayoutSuggestion]
        BUYER_GETS_TRADE_AMOUNT: _ClassVar[DisputeResult.PayoutSuggestion]
        BUYER_GETS_TRADE_AMOUNT_PLUS_COMPENSATION: _ClassVar[DisputeResult.PayoutSuggestion]
        BUYER_GETS_TRADE_AMOUNT_MINUS_PENALTY: _ClassVar[DisputeResult.PayoutSuggestion]
        SELLER_GETS_TRADE_AMOUNT: _ClassVar[DisputeResult.PayoutSuggestion]
        SELLER_GETS_TRADE_AMOUNT_PLUS_COMPENSATION: _ClassVar[DisputeResult.PayoutSuggestion]
        SELLER_GETS_TRADE_AMOUNT_MINUS_PENALTY: _ClassVar[DisputeResult.PayoutSuggestion]
    CUSTOM_PAYOUT: DisputeResult.PayoutSuggestion
    BUYER_GETS_TRADE_AMOUNT: DisputeResult.PayoutSuggestion
    BUYER_GETS_TRADE_AMOUNT_PLUS_COMPENSATION: DisputeResult.PayoutSuggestion
    BUYER_GETS_TRADE_AMOUNT_MINUS_PENALTY: DisputeResult.PayoutSuggestion
    SELLER_GETS_TRADE_AMOUNT: DisputeResult.PayoutSuggestion
    SELLER_GETS_TRADE_AMOUNT_PLUS_COMPENSATION: DisputeResult.PayoutSuggestion
    SELLER_GETS_TRADE_AMOUNT_MINUS_PENALTY: DisputeResult.PayoutSuggestion
    TRADE_ID_FIELD_NUMBER: _ClassVar[int]
    TRADER_ID_FIELD_NUMBER: _ClassVar[int]
    WINNER_FIELD_NUMBER: _ClassVar[int]
    REASON_ORDINAL_FIELD_NUMBER: _ClassVar[int]
    TAMPER_PROOF_EVIDENCE_FIELD_NUMBER: _ClassVar[int]
    ID_VERIFICATION_FIELD_NUMBER: _ClassVar[int]
    SCREEN_CAST_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_NOTES_FIELD_NUMBER: _ClassVar[int]
    CHAT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ARBITRATOR_SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    BUYER_PAYOUT_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    SELLER_PAYOUT_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    ARBITRATOR_PUB_KEY_FIELD_NUMBER: _ClassVar[int]
    CLOSE_DATE_FIELD_NUMBER: _ClassVar[int]
    IS_LOSER_PUBLISHER_FIELD_NUMBER: _ClassVar[int]
    PAYOUT_ADJUSTMENT_PERCENT_FIELD_NUMBER: _ClassVar[int]
    PAYOUT_SUGGESTION_FIELD_NUMBER: _ClassVar[int]
    trade_id: str
    trader_id: int
    winner: DisputeResult.Winner
    reason_ordinal: int
    tamper_proof_evidence: bool
    id_verification: bool
    screen_cast: bool
    summary_notes: str
    chat_message: ChatMessage
    arbitrator_signature: bytes
    buyer_payout_amount: int
    seller_payout_amount: int
    arbitrator_pub_key: bytes
    close_date: int
    is_loser_publisher: bool
    payout_adjustment_percent: str
    payout_suggestion: DisputeResult.PayoutSuggestion
    def __init__(self, trade_id: _Optional[str] = ..., trader_id: _Optional[int] = ..., winner: _Optional[_Union[DisputeResult.Winner, str]] = ..., reason_ordinal: _Optional[int] = ..., tamper_proof_evidence: bool = ..., id_verification: bool = ..., screen_cast: bool = ..., summary_notes: _Optional[str] = ..., chat_message: _Optional[_Union[ChatMessage, _Mapping]] = ..., arbitrator_signature: _Optional[bytes] = ..., buyer_payout_amount: _Optional[int] = ..., seller_payout_amount: _Optional[int] = ..., arbitrator_pub_key: _Optional[bytes] = ..., close_date: _Optional[int] = ..., is_loser_publisher: bool = ..., payout_adjustment_percent: _Optional[str] = ..., payout_suggestion: _Optional[_Union[DisputeResult.PayoutSuggestion, str]] = ...) -> None: ...

class Contract(_message.Message):
    __slots__ = ("offer_payload", "trade_amount", "trade_price", "taker_fee_tx_id", "is_buyer_maker_and_seller_taker", "maker_account_id", "taker_account_id", "maker_payment_account_payload", "taker_payment_account_payload", "maker_pub_key_ring", "taker_pub_key_ring", "buyer_node_address", "seller_node_address", "maker_payout_address_string", "taker_payout_address_string", "maker_multi_sig_pub_key", "taker_multi_sig_pub_key", "mediator_node_address", "lock_time", "refund_agent_node_address", "hash_of_makers_payment_account_payload", "hash_of_takers_payment_account_payload", "maker_payment_method_id", "taker_payment_method_id")
    OFFER_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    TRADE_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    TRADE_PRICE_FIELD_NUMBER: _ClassVar[int]
    TAKER_FEE_TX_ID_FIELD_NUMBER: _ClassVar[int]
    IS_BUYER_MAKER_AND_SELLER_TAKER_FIELD_NUMBER: _ClassVar[int]
    MAKER_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    TAKER_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    MAKER_PAYMENT_ACCOUNT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    TAKER_PAYMENT_ACCOUNT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    MAKER_PUB_KEY_RING_FIELD_NUMBER: _ClassVar[int]
    TAKER_PUB_KEY_RING_FIELD_NUMBER: _ClassVar[int]
    BUYER_NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    SELLER_NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    MAKER_PAYOUT_ADDRESS_STRING_FIELD_NUMBER: _ClassVar[int]
    TAKER_PAYOUT_ADDRESS_STRING_FIELD_NUMBER: _ClassVar[int]
    MAKER_MULTI_SIG_PUB_KEY_FIELD_NUMBER: _ClassVar[int]
    TAKER_MULTI_SIG_PUB_KEY_FIELD_NUMBER: _ClassVar[int]
    MEDIATOR_NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    LOCK_TIME_FIELD_NUMBER: _ClassVar[int]
    REFUND_AGENT_NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    HASH_OF_MAKERS_PAYMENT_ACCOUNT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    HASH_OF_TAKERS_PAYMENT_ACCOUNT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    MAKER_PAYMENT_METHOD_ID_FIELD_NUMBER: _ClassVar[int]
    TAKER_PAYMENT_METHOD_ID_FIELD_NUMBER: _ClassVar[int]
    offer_payload: OfferPayload
    trade_amount: int
    trade_price: int
    taker_fee_tx_id: str
    is_buyer_maker_and_seller_taker: bool
    maker_account_id: str
    taker_account_id: str
    maker_payment_account_payload: PaymentAccountPayload
    taker_payment_account_payload: PaymentAccountPayload
    maker_pub_key_ring: PubKeyRing
    taker_pub_key_ring: PubKeyRing
    buyer_node_address: NodeAddress
    seller_node_address: NodeAddress
    maker_payout_address_string: str
    taker_payout_address_string: str
    maker_multi_sig_pub_key: bytes
    taker_multi_sig_pub_key: bytes
    mediator_node_address: NodeAddress
    lock_time: int
    refund_agent_node_address: NodeAddress
    hash_of_makers_payment_account_payload: bytes
    hash_of_takers_payment_account_payload: bytes
    maker_payment_method_id: str
    taker_payment_method_id: str
    def __init__(self, offer_payload: _Optional[_Union[OfferPayload, _Mapping]] = ..., trade_amount: _Optional[int] = ..., trade_price: _Optional[int] = ..., taker_fee_tx_id: _Optional[str] = ..., is_buyer_maker_and_seller_taker: bool = ..., maker_account_id: _Optional[str] = ..., taker_account_id: _Optional[str] = ..., maker_payment_account_payload: _Optional[_Union[PaymentAccountPayload, _Mapping]] = ..., taker_payment_account_payload: _Optional[_Union[PaymentAccountPayload, _Mapping]] = ..., maker_pub_key_ring: _Optional[_Union[PubKeyRing, _Mapping]] = ..., taker_pub_key_ring: _Optional[_Union[PubKeyRing, _Mapping]] = ..., buyer_node_address: _Optional[_Union[NodeAddress, _Mapping]] = ..., seller_node_address: _Optional[_Union[NodeAddress, _Mapping]] = ..., maker_payout_address_string: _Optional[str] = ..., taker_payout_address_string: _Optional[str] = ..., maker_multi_sig_pub_key: _Optional[bytes] = ..., taker_multi_sig_pub_key: _Optional[bytes] = ..., mediator_node_address: _Optional[_Union[NodeAddress, _Mapping]] = ..., lock_time: _Optional[int] = ..., refund_agent_node_address: _Optional[_Union[NodeAddress, _Mapping]] = ..., hash_of_makers_payment_account_payload: _Optional[bytes] = ..., hash_of_takers_payment_account_payload: _Optional[bytes] = ..., maker_payment_method_id: _Optional[str] = ..., taker_payment_method_id: _Optional[str] = ...) -> None: ...

class RawTransactionInput(_message.Message):
    __slots__ = ("index", "parent_transaction", "value", "script_type_id")
    INDEX_FIELD_NUMBER: _ClassVar[int]
    PARENT_TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    index: int
    parent_transaction: bytes
    value: int
    script_type_id: int
    def __init__(self, index: _Optional[int] = ..., parent_transaction: _Optional[bytes] = ..., value: _Optional[int] = ..., script_type_id: _Optional[int] = ...) -> None: ...

class PaymentAccountPayload(_message.Message):
    __slots__ = ("id", "payment_method_id", "max_trade_period", "ali_pay_account_payload", "chase_quick_pay_account_payload", "clear_xchange_account_payload", "country_based_payment_account_payload", "crypto_currency_account_payload", "faster_payments_account_payload", "interac_e_transfer_account_payload", "o_k_pay_account_payload", "perfect_money_account_payload", "swish_account_payload", "u_s_postal_money_order_account_payload", "uphold_account_payload", "cash_app_account_payload", "money_beam_account_payload", "venmo_account_payload", "popmoney_account_payload", "revolut_account_payload", "we_chat_pay_account_payload", "money_gram_account_payload", "hal_cash_account_payload", "prompt_pay_account_payload", "advanced_cash_account_payload", "instant_crypto_currency_account_payload", "japan_bank_account_payload", "Transferwise_account_payload", "australia_payid_payload", "amazon_gift_card_account_payload", "cash_by_mail_account_payload", "capitual_account_payload", "Paysera_account_payload", "Paxum_account_payload", "swift_account_payload", "cel_pay_account_payload", "monese_account_payload", "verse_account_payload", "bsq_swap_account_payload", "sbp_account_payload", "exclude_from_json_data")
    class ExcludeFromJsonDataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_METHOD_ID_FIELD_NUMBER: _ClassVar[int]
    MAX_TRADE_PERIOD_FIELD_NUMBER: _ClassVar[int]
    ALI_PAY_ACCOUNT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    CHASE_QUICK_PAY_ACCOUNT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    CLEAR_XCHANGE_ACCOUNT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_BASED_PAYMENT_ACCOUNT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    CRYPTO_CURRENCY_ACCOUNT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    FASTER_PAYMENTS_ACCOUNT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    INTERAC_E_TRANSFER_ACCOUNT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    O_K_PAY_ACCOUNT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    PERFECT_MONEY_ACCOUNT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    SWISH_ACCOUNT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    U_S_POSTAL_MONEY_ORDER_ACCOUNT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    UPHOLD_ACCOUNT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    CASH_APP_ACCOUNT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    MONEY_BEAM_ACCOUNT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    VENMO_ACCOUNT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    POPMONEY_ACCOUNT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    REVOLUT_ACCOUNT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    WE_CHAT_PAY_ACCOUNT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    MONEY_GRAM_ACCOUNT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    HAL_CASH_ACCOUNT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    PROMPT_PAY_ACCOUNT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    ADVANCED_CASH_ACCOUNT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    INSTANT_CRYPTO_CURRENCY_ACCOUNT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    JAPAN_BANK_ACCOUNT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    TRANSFERWISE_ACCOUNT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    AUSTRALIA_PAYID_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    AMAZON_GIFT_CARD_ACCOUNT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    CASH_BY_MAIL_ACCOUNT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    CAPITUAL_ACCOUNT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    PAYSERA_ACCOUNT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    PAXUM_ACCOUNT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    SWIFT_ACCOUNT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    CEL_PAY_ACCOUNT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    MONESE_ACCOUNT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    VERSE_ACCOUNT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    BSQ_SWAP_ACCOUNT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    SBP_ACCOUNT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_FROM_JSON_DATA_FIELD_NUMBER: _ClassVar[int]
    id: str
    payment_method_id: str
    max_trade_period: int
    ali_pay_account_payload: AliPayAccountPayload
    chase_quick_pay_account_payload: ChaseQuickPayAccountPayload
    clear_xchange_account_payload: ClearXchangeAccountPayload
    country_based_payment_account_payload: CountryBasedPaymentAccountPayload
    crypto_currency_account_payload: CryptoCurrencyAccountPayload
    faster_payments_account_payload: FasterPaymentsAccountPayload
    interac_e_transfer_account_payload: InteracETransferAccountPayload
    o_k_pay_account_payload: OKPayAccountPayload
    perfect_money_account_payload: PerfectMoneyAccountPayload
    swish_account_payload: SwishAccountPayload
    u_s_postal_money_order_account_payload: USPostalMoneyOrderAccountPayload
    uphold_account_payload: UpholdAccountPayload
    cash_app_account_payload: CashAppAccountPayload
    money_beam_account_payload: MoneyBeamAccountPayload
    venmo_account_payload: VenmoAccountPayload
    popmoney_account_payload: PopmoneyAccountPayload
    revolut_account_payload: RevolutAccountPayload
    we_chat_pay_account_payload: WeChatPayAccountPayload
    money_gram_account_payload: MoneyGramAccountPayload
    hal_cash_account_payload: HalCashAccountPayload
    prompt_pay_account_payload: PromptPayAccountPayload
    advanced_cash_account_payload: AdvancedCashAccountPayload
    instant_crypto_currency_account_payload: InstantCryptoCurrencyAccountPayload
    japan_bank_account_payload: JapanBankAccountPayload
    Transferwise_account_payload: TransferwiseAccountPayload
    australia_payid_payload: AustraliaPayidPayload
    amazon_gift_card_account_payload: AmazonGiftCardAccountPayload
    cash_by_mail_account_payload: CashByMailAccountPayload
    capitual_account_payload: CapitualAccountPayload
    Paysera_account_payload: PayseraAccountPayload
    Paxum_account_payload: PaxumAccountPayload
    swift_account_payload: SwiftAccountPayload
    cel_pay_account_payload: CelPayAccountPayload
    monese_account_payload: MoneseAccountPayload
    verse_account_payload: VerseAccountPayload
    bsq_swap_account_payload: BsqSwapAccountPayload
    sbp_account_payload: SbpAccountPayload
    exclude_from_json_data: _containers.ScalarMap[str, str]
    def __init__(self, id: _Optional[str] = ..., payment_method_id: _Optional[str] = ..., max_trade_period: _Optional[int] = ..., ali_pay_account_payload: _Optional[_Union[AliPayAccountPayload, _Mapping]] = ..., chase_quick_pay_account_payload: _Optional[_Union[ChaseQuickPayAccountPayload, _Mapping]] = ..., clear_xchange_account_payload: _Optional[_Union[ClearXchangeAccountPayload, _Mapping]] = ..., country_based_payment_account_payload: _Optional[_Union[CountryBasedPaymentAccountPayload, _Mapping]] = ..., crypto_currency_account_payload: _Optional[_Union[CryptoCurrencyAccountPayload, _Mapping]] = ..., faster_payments_account_payload: _Optional[_Union[FasterPaymentsAccountPayload, _Mapping]] = ..., interac_e_transfer_account_payload: _Optional[_Union[InteracETransferAccountPayload, _Mapping]] = ..., o_k_pay_account_payload: _Optional[_Union[OKPayAccountPayload, _Mapping]] = ..., perfect_money_account_payload: _Optional[_Union[PerfectMoneyAccountPayload, _Mapping]] = ..., swish_account_payload: _Optional[_Union[SwishAccountPayload, _Mapping]] = ..., u_s_postal_money_order_account_payload: _Optional[_Union[USPostalMoneyOrderAccountPayload, _Mapping]] = ..., uphold_account_payload: _Optional[_Union[UpholdAccountPayload, _Mapping]] = ..., cash_app_account_payload: _Optional[_Union[CashAppAccountPayload, _Mapping]] = ..., money_beam_account_payload: _Optional[_Union[MoneyBeamAccountPayload, _Mapping]] = ..., venmo_account_payload: _Optional[_Union[VenmoAccountPayload, _Mapping]] = ..., popmoney_account_payload: _Optional[_Union[PopmoneyAccountPayload, _Mapping]] = ..., revolut_account_payload: _Optional[_Union[RevolutAccountPayload, _Mapping]] = ..., we_chat_pay_account_payload: _Optional[_Union[WeChatPayAccountPayload, _Mapping]] = ..., money_gram_account_payload: _Optional[_Union[MoneyGramAccountPayload, _Mapping]] = ..., hal_cash_account_payload: _Optional[_Union[HalCashAccountPayload, _Mapping]] = ..., prompt_pay_account_payload: _Optional[_Union[PromptPayAccountPayload, _Mapping]] = ..., advanced_cash_account_payload: _Optional[_Union[AdvancedCashAccountPayload, _Mapping]] = ..., instant_crypto_currency_account_payload: _Optional[_Union[InstantCryptoCurrencyAccountPayload, _Mapping]] = ..., japan_bank_account_payload: _Optional[_Union[JapanBankAccountPayload, _Mapping]] = ..., Transferwise_account_payload: _Optional[_Union[TransferwiseAccountPayload, _Mapping]] = ..., australia_payid_payload: _Optional[_Union[AustraliaPayidPayload, _Mapping]] = ..., amazon_gift_card_account_payload: _Optional[_Union[AmazonGiftCardAccountPayload, _Mapping]] = ..., cash_by_mail_account_payload: _Optional[_Union[CashByMailAccountPayload, _Mapping]] = ..., capitual_account_payload: _Optional[_Union[CapitualAccountPayload, _Mapping]] = ..., Paysera_account_payload: _Optional[_Union[PayseraAccountPayload, _Mapping]] = ..., Paxum_account_payload: _Optional[_Union[PaxumAccountPayload, _Mapping]] = ..., swift_account_payload: _Optional[_Union[SwiftAccountPayload, _Mapping]] = ..., cel_pay_account_payload: _Optional[_Union[CelPayAccountPayload, _Mapping]] = ..., monese_account_payload: _Optional[_Union[MoneseAccountPayload, _Mapping]] = ..., verse_account_payload: _Optional[_Union[VerseAccountPayload, _Mapping]] = ..., bsq_swap_account_payload: _Optional[_Union[BsqSwapAccountPayload, _Mapping]] = ..., sbp_account_payload: _Optional[_Union[SbpAccountPayload, _Mapping]] = ..., exclude_from_json_data: _Optional[_Mapping[str, str]] = ...) -> None: ...

class AliPayAccountPayload(_message.Message):
    __slots__ = ("account_nr",)
    ACCOUNT_NR_FIELD_NUMBER: _ClassVar[int]
    account_nr: str
    def __init__(self, account_nr: _Optional[str] = ...) -> None: ...

class WeChatPayAccountPayload(_message.Message):
    __slots__ = ("account_nr",)
    ACCOUNT_NR_FIELD_NUMBER: _ClassVar[int]
    account_nr: str
    def __init__(self, account_nr: _Optional[str] = ...) -> None: ...

class ChaseQuickPayAccountPayload(_message.Message):
    __slots__ = ("email", "holder_name")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    HOLDER_NAME_FIELD_NUMBER: _ClassVar[int]
    email: str
    holder_name: str
    def __init__(self, email: _Optional[str] = ..., holder_name: _Optional[str] = ...) -> None: ...

class ClearXchangeAccountPayload(_message.Message):
    __slots__ = ("holder_name", "email_or_mobile_nr")
    HOLDER_NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_OR_MOBILE_NR_FIELD_NUMBER: _ClassVar[int]
    holder_name: str
    email_or_mobile_nr: str
    def __init__(self, holder_name: _Optional[str] = ..., email_or_mobile_nr: _Optional[str] = ...) -> None: ...

class CountryBasedPaymentAccountPayload(_message.Message):
    __slots__ = ("countryCode", "bank_account_payload", "cash_deposit_account_payload", "sepa_account_payload", "western_union_account_payload", "sepa_instant_account_payload", "f2f_account_payload", "upi_account_payload", "paytm_account_payload", "ifsc_based_account_payload", "nequi_account_payload", "bizum_account_payload", "pix_account_payload", "satispay_account_payload", "strike_account_payload", "tikkie_account_payload", "transferwise_usd_account_payload", "mercado_pago_account_payload")
    COUNTRYCODE_FIELD_NUMBER: _ClassVar[int]
    BANK_ACCOUNT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    CASH_DEPOSIT_ACCOUNT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    SEPA_ACCOUNT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    WESTERN_UNION_ACCOUNT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    SEPA_INSTANT_ACCOUNT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    F2F_ACCOUNT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    UPI_ACCOUNT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    PAYTM_ACCOUNT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    IFSC_BASED_ACCOUNT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    NEQUI_ACCOUNT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    BIZUM_ACCOUNT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    PIX_ACCOUNT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    SATISPAY_ACCOUNT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    STRIKE_ACCOUNT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    TIKKIE_ACCOUNT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    TRANSFERWISE_USD_ACCOUNT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    MERCADO_PAGO_ACCOUNT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    countryCode: str
    bank_account_payload: BankAccountPayload
    cash_deposit_account_payload: CashDepositAccountPayload
    sepa_account_payload: SepaAccountPayload
    western_union_account_payload: WesternUnionAccountPayload
    sepa_instant_account_payload: SepaInstantAccountPayload
    f2f_account_payload: F2FAccountPayload
    upi_account_payload: UpiAccountPayload
    paytm_account_payload: PaytmAccountPayload
    ifsc_based_account_payload: IfscBasedAccountPayload
    nequi_account_payload: NequiAccountPayload
    bizum_account_payload: BizumAccountPayload
    pix_account_payload: PixAccountPayload
    satispay_account_payload: SatispayAccountPayload
    strike_account_payload: StrikeAccountPayload
    tikkie_account_payload: TikkieAccountPayload
    transferwise_usd_account_payload: TransferwiseUsdAccountPayload
    mercado_pago_account_payload: MercadoPagoAccountPayload
    def __init__(self, countryCode: _Optional[str] = ..., bank_account_payload: _Optional[_Union[BankAccountPayload, _Mapping]] = ..., cash_deposit_account_payload: _Optional[_Union[CashDepositAccountPayload, _Mapping]] = ..., sepa_account_payload: _Optional[_Union[SepaAccountPayload, _Mapping]] = ..., western_union_account_payload: _Optional[_Union[WesternUnionAccountPayload, _Mapping]] = ..., sepa_instant_account_payload: _Optional[_Union[SepaInstantAccountPayload, _Mapping]] = ..., f2f_account_payload: _Optional[_Union[F2FAccountPayload, _Mapping]] = ..., upi_account_payload: _Optional[_Union[UpiAccountPayload, _Mapping]] = ..., paytm_account_payload: _Optional[_Union[PaytmAccountPayload, _Mapping]] = ..., ifsc_based_account_payload: _Optional[_Union[IfscBasedAccountPayload, _Mapping]] = ..., nequi_account_payload: _Optional[_Union[NequiAccountPayload, _Mapping]] = ..., bizum_account_payload: _Optional[_Union[BizumAccountPayload, _Mapping]] = ..., pix_account_payload: _Optional[_Union[PixAccountPayload, _Mapping]] = ..., satispay_account_payload: _Optional[_Union[SatispayAccountPayload, _Mapping]] = ..., strike_account_payload: _Optional[_Union[StrikeAccountPayload, _Mapping]] = ..., tikkie_account_payload: _Optional[_Union[TikkieAccountPayload, _Mapping]] = ..., transferwise_usd_account_payload: _Optional[_Union[TransferwiseUsdAccountPayload, _Mapping]] = ..., mercado_pago_account_payload: _Optional[_Union[MercadoPagoAccountPayload, _Mapping]] = ...) -> None: ...

class BankAccountPayload(_message.Message):
    __slots__ = ("holder_name", "bank_name", "bank_id", "branch_id", "account_nr", "account_type", "holder_tax_id", "email", "national_bank_account_payload", "same_bank_accont_payload", "specific_banks_account_payload", "ach_transfer_account_payload", "domestic_wire_transfer_account_payload", "national_account_id")
    HOLDER_NAME_FIELD_NUMBER: _ClassVar[int]
    BANK_NAME_FIELD_NUMBER: _ClassVar[int]
    BANK_ID_FIELD_NUMBER: _ClassVar[int]
    BRANCH_ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_NR_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_TYPE_FIELD_NUMBER: _ClassVar[int]
    HOLDER_TAX_ID_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    NATIONAL_BANK_ACCOUNT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    SAME_BANK_ACCONT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    SPECIFIC_BANKS_ACCOUNT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    ACH_TRANSFER_ACCOUNT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    DOMESTIC_WIRE_TRANSFER_ACCOUNT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    NATIONAL_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    holder_name: str
    bank_name: str
    bank_id: str
    branch_id: str
    account_nr: str
    account_type: str
    holder_tax_id: str
    email: str
    national_bank_account_payload: NationalBankAccountPayload
    same_bank_accont_payload: SameBankAccountPayload
    specific_banks_account_payload: SpecificBanksAccountPayload
    ach_transfer_account_payload: AchTransferAccountPayload
    domestic_wire_transfer_account_payload: DomesticWireTransferAccountPayload
    national_account_id: str
    def __init__(self, holder_name: _Optional[str] = ..., bank_name: _Optional[str] = ..., bank_id: _Optional[str] = ..., branch_id: _Optional[str] = ..., account_nr: _Optional[str] = ..., account_type: _Optional[str] = ..., holder_tax_id: _Optional[str] = ..., email: _Optional[str] = ..., national_bank_account_payload: _Optional[_Union[NationalBankAccountPayload, _Mapping]] = ..., same_bank_accont_payload: _Optional[_Union[SameBankAccountPayload, _Mapping]] = ..., specific_banks_account_payload: _Optional[_Union[SpecificBanksAccountPayload, _Mapping]] = ..., ach_transfer_account_payload: _Optional[_Union[AchTransferAccountPayload, _Mapping]] = ..., domestic_wire_transfer_account_payload: _Optional[_Union[DomesticWireTransferAccountPayload, _Mapping]] = ..., national_account_id: _Optional[str] = ...) -> None: ...

class AchTransferAccountPayload(_message.Message):
    __slots__ = ("holder_address",)
    HOLDER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    holder_address: str
    def __init__(self, holder_address: _Optional[str] = ...) -> None: ...

class DomesticWireTransferAccountPayload(_message.Message):
    __slots__ = ("holder_address",)
    HOLDER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    holder_address: str
    def __init__(self, holder_address: _Optional[str] = ...) -> None: ...

class NationalBankAccountPayload(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SameBankAccountPayload(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class JapanBankAccountPayload(_message.Message):
    __slots__ = ("bank_name", "bank_code", "bank_branch_name", "bank_branch_code", "bank_account_type", "bank_account_name", "bank_account_number")
    BANK_NAME_FIELD_NUMBER: _ClassVar[int]
    BANK_CODE_FIELD_NUMBER: _ClassVar[int]
    BANK_BRANCH_NAME_FIELD_NUMBER: _ClassVar[int]
    BANK_BRANCH_CODE_FIELD_NUMBER: _ClassVar[int]
    BANK_ACCOUNT_TYPE_FIELD_NUMBER: _ClassVar[int]
    BANK_ACCOUNT_NAME_FIELD_NUMBER: _ClassVar[int]
    BANK_ACCOUNT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    bank_name: str
    bank_code: str
    bank_branch_name: str
    bank_branch_code: str
    bank_account_type: str
    bank_account_name: str
    bank_account_number: str
    def __init__(self, bank_name: _Optional[str] = ..., bank_code: _Optional[str] = ..., bank_branch_name: _Optional[str] = ..., bank_branch_code: _Optional[str] = ..., bank_account_type: _Optional[str] = ..., bank_account_name: _Optional[str] = ..., bank_account_number: _Optional[str] = ...) -> None: ...

class AustraliaPayidPayload(_message.Message):
    __slots__ = ("bank_account_name", "payid")
    BANK_ACCOUNT_NAME_FIELD_NUMBER: _ClassVar[int]
    PAYID_FIELD_NUMBER: _ClassVar[int]
    bank_account_name: str
    payid: str
    def __init__(self, bank_account_name: _Optional[str] = ..., payid: _Optional[str] = ...) -> None: ...

class SpecificBanksAccountPayload(_message.Message):
    __slots__ = ("accepted_banks",)
    ACCEPTED_BANKS_FIELD_NUMBER: _ClassVar[int]
    accepted_banks: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, accepted_banks: _Optional[_Iterable[str]] = ...) -> None: ...

class CashDepositAccountPayload(_message.Message):
    __slots__ = ("holder_name", "holder_email", "bank_name", "bank_id", "branch_id", "account_nr", "account_type", "requirements", "holder_tax_id", "national_account_id")
    HOLDER_NAME_FIELD_NUMBER: _ClassVar[int]
    HOLDER_EMAIL_FIELD_NUMBER: _ClassVar[int]
    BANK_NAME_FIELD_NUMBER: _ClassVar[int]
    BANK_ID_FIELD_NUMBER: _ClassVar[int]
    BRANCH_ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_NR_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_TYPE_FIELD_NUMBER: _ClassVar[int]
    REQUIREMENTS_FIELD_NUMBER: _ClassVar[int]
    HOLDER_TAX_ID_FIELD_NUMBER: _ClassVar[int]
    NATIONAL_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    holder_name: str
    holder_email: str
    bank_name: str
    bank_id: str
    branch_id: str
    account_nr: str
    account_type: str
    requirements: str
    holder_tax_id: str
    national_account_id: str
    def __init__(self, holder_name: _Optional[str] = ..., holder_email: _Optional[str] = ..., bank_name: _Optional[str] = ..., bank_id: _Optional[str] = ..., branch_id: _Optional[str] = ..., account_nr: _Optional[str] = ..., account_type: _Optional[str] = ..., requirements: _Optional[str] = ..., holder_tax_id: _Optional[str] = ..., national_account_id: _Optional[str] = ...) -> None: ...

class MoneyGramAccountPayload(_message.Message):
    __slots__ = ("holder_name", "country_code", "state", "email")
    HOLDER_NAME_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    holder_name: str
    country_code: str
    state: str
    email: str
    def __init__(self, holder_name: _Optional[str] = ..., country_code: _Optional[str] = ..., state: _Optional[str] = ..., email: _Optional[str] = ...) -> None: ...

class HalCashAccountPayload(_message.Message):
    __slots__ = ("mobile_nr",)
    MOBILE_NR_FIELD_NUMBER: _ClassVar[int]
    mobile_nr: str
    def __init__(self, mobile_nr: _Optional[str] = ...) -> None: ...

class WesternUnionAccountPayload(_message.Message):
    __slots__ = ("holder_name", "city", "state", "email")
    HOLDER_NAME_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    holder_name: str
    city: str
    state: str
    email: str
    def __init__(self, holder_name: _Optional[str] = ..., city: _Optional[str] = ..., state: _Optional[str] = ..., email: _Optional[str] = ...) -> None: ...

class AmazonGiftCardAccountPayload(_message.Message):
    __slots__ = ("email_or_mobile_nr", "country_code")
    EMAIL_OR_MOBILE_NR_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    email_or_mobile_nr: str
    country_code: str
    def __init__(self, email_or_mobile_nr: _Optional[str] = ..., country_code: _Optional[str] = ...) -> None: ...

class SepaAccountPayload(_message.Message):
    __slots__ = ("holder_name", "iban", "bic", "email", "accepted_country_codes")
    HOLDER_NAME_FIELD_NUMBER: _ClassVar[int]
    IBAN_FIELD_NUMBER: _ClassVar[int]
    BIC_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    ACCEPTED_COUNTRY_CODES_FIELD_NUMBER: _ClassVar[int]
    holder_name: str
    iban: str
    bic: str
    email: str
    accepted_country_codes: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, holder_name: _Optional[str] = ..., iban: _Optional[str] = ..., bic: _Optional[str] = ..., email: _Optional[str] = ..., accepted_country_codes: _Optional[_Iterable[str]] = ...) -> None: ...

class SepaInstantAccountPayload(_message.Message):
    __slots__ = ("holder_name", "iban", "bic", "accepted_country_codes")
    HOLDER_NAME_FIELD_NUMBER: _ClassVar[int]
    IBAN_FIELD_NUMBER: _ClassVar[int]
    BIC_FIELD_NUMBER: _ClassVar[int]
    ACCEPTED_COUNTRY_CODES_FIELD_NUMBER: _ClassVar[int]
    holder_name: str
    iban: str
    bic: str
    accepted_country_codes: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, holder_name: _Optional[str] = ..., iban: _Optional[str] = ..., bic: _Optional[str] = ..., accepted_country_codes: _Optional[_Iterable[str]] = ...) -> None: ...

class CryptoCurrencyAccountPayload(_message.Message):
    __slots__ = ("address",)
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    address: str
    def __init__(self, address: _Optional[str] = ...) -> None: ...

class InstantCryptoCurrencyAccountPayload(_message.Message):
    __slots__ = ("address",)
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    address: str
    def __init__(self, address: _Optional[str] = ...) -> None: ...

class BsqSwapAccountPayload(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FasterPaymentsAccountPayload(_message.Message):
    __slots__ = ("sort_code", "account_nr", "email")
    SORT_CODE_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_NR_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    sort_code: str
    account_nr: str
    email: str
    def __init__(self, sort_code: _Optional[str] = ..., account_nr: _Optional[str] = ..., email: _Optional[str] = ...) -> None: ...

class InteracETransferAccountPayload(_message.Message):
    __slots__ = ("email", "holder_name", "question", "answer")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    HOLDER_NAME_FIELD_NUMBER: _ClassVar[int]
    QUESTION_FIELD_NUMBER: _ClassVar[int]
    ANSWER_FIELD_NUMBER: _ClassVar[int]
    email: str
    holder_name: str
    question: str
    answer: str
    def __init__(self, email: _Optional[str] = ..., holder_name: _Optional[str] = ..., question: _Optional[str] = ..., answer: _Optional[str] = ...) -> None: ...

class OKPayAccountPayload(_message.Message):
    __slots__ = ("account_nr",)
    ACCOUNT_NR_FIELD_NUMBER: _ClassVar[int]
    account_nr: str
    def __init__(self, account_nr: _Optional[str] = ...) -> None: ...

class UpholdAccountPayload(_message.Message):
    __slots__ = ("account_id", "account_owner")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_OWNER_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    account_owner: str
    def __init__(self, account_id: _Optional[str] = ..., account_owner: _Optional[str] = ...) -> None: ...

class CashAppAccountPayload(_message.Message):
    __slots__ = ("cash_tag",)
    CASH_TAG_FIELD_NUMBER: _ClassVar[int]
    cash_tag: str
    def __init__(self, cash_tag: _Optional[str] = ...) -> None: ...

class MoneyBeamAccountPayload(_message.Message):
    __slots__ = ("account_id",)
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    def __init__(self, account_id: _Optional[str] = ...) -> None: ...

class VenmoAccountPayload(_message.Message):
    __slots__ = ("venmo_user_name", "holder_name")
    VENMO_USER_NAME_FIELD_NUMBER: _ClassVar[int]
    HOLDER_NAME_FIELD_NUMBER: _ClassVar[int]
    venmo_user_name: str
    holder_name: str
    def __init__(self, venmo_user_name: _Optional[str] = ..., holder_name: _Optional[str] = ...) -> None: ...

class PopmoneyAccountPayload(_message.Message):
    __slots__ = ("account_id", "holder_name")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    HOLDER_NAME_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    holder_name: str
    def __init__(self, account_id: _Optional[str] = ..., holder_name: _Optional[str] = ...) -> None: ...

class RevolutAccountPayload(_message.Message):
    __slots__ = ("account_id", "user_name")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    user_name: str
    def __init__(self, account_id: _Optional[str] = ..., user_name: _Optional[str] = ...) -> None: ...

class PerfectMoneyAccountPayload(_message.Message):
    __slots__ = ("account_nr",)
    ACCOUNT_NR_FIELD_NUMBER: _ClassVar[int]
    account_nr: str
    def __init__(self, account_nr: _Optional[str] = ...) -> None: ...

class SwishAccountPayload(_message.Message):
    __slots__ = ("mobile_nr", "holder_name")
    MOBILE_NR_FIELD_NUMBER: _ClassVar[int]
    HOLDER_NAME_FIELD_NUMBER: _ClassVar[int]
    mobile_nr: str
    holder_name: str
    def __init__(self, mobile_nr: _Optional[str] = ..., holder_name: _Optional[str] = ...) -> None: ...

class USPostalMoneyOrderAccountPayload(_message.Message):
    __slots__ = ("postal_address", "holder_name")
    POSTAL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    HOLDER_NAME_FIELD_NUMBER: _ClassVar[int]
    postal_address: str
    holder_name: str
    def __init__(self, postal_address: _Optional[str] = ..., holder_name: _Optional[str] = ...) -> None: ...

class F2FAccountPayload(_message.Message):
    __slots__ = ("contact", "city", "extra_info")
    CONTACT_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    EXTRA_INFO_FIELD_NUMBER: _ClassVar[int]
    contact: str
    city: str
    extra_info: str
    def __init__(self, contact: _Optional[str] = ..., city: _Optional[str] = ..., extra_info: _Optional[str] = ...) -> None: ...

class IfscBasedAccountPayload(_message.Message):
    __slots__ = ("holder_name", "account_nr", "ifsc", "neft_account_payload", "rtgs_account_payload", "imps_account_payload")
    HOLDER_NAME_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_NR_FIELD_NUMBER: _ClassVar[int]
    IFSC_FIELD_NUMBER: _ClassVar[int]
    NEFT_ACCOUNT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    RTGS_ACCOUNT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    IMPS_ACCOUNT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    holder_name: str
    account_nr: str
    ifsc: str
    neft_account_payload: NeftAccountPayload
    rtgs_account_payload: RtgsAccountPayload
    imps_account_payload: ImpsAccountPayload
    def __init__(self, holder_name: _Optional[str] = ..., account_nr: _Optional[str] = ..., ifsc: _Optional[str] = ..., neft_account_payload: _Optional[_Union[NeftAccountPayload, _Mapping]] = ..., rtgs_account_payload: _Optional[_Union[RtgsAccountPayload, _Mapping]] = ..., imps_account_payload: _Optional[_Union[ImpsAccountPayload, _Mapping]] = ...) -> None: ...

class NeftAccountPayload(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RtgsAccountPayload(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ImpsAccountPayload(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpiAccountPayload(_message.Message):
    __slots__ = ("virtual_payment_address",)
    VIRTUAL_PAYMENT_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    virtual_payment_address: str
    def __init__(self, virtual_payment_address: _Optional[str] = ...) -> None: ...

class PaytmAccountPayload(_message.Message):
    __slots__ = ("email_or_mobile_nr",)
    EMAIL_OR_MOBILE_NR_FIELD_NUMBER: _ClassVar[int]
    email_or_mobile_nr: str
    def __init__(self, email_or_mobile_nr: _Optional[str] = ...) -> None: ...

class CashByMailAccountPayload(_message.Message):
    __slots__ = ("postal_address", "contact", "extra_info")
    POSTAL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    CONTACT_FIELD_NUMBER: _ClassVar[int]
    EXTRA_INFO_FIELD_NUMBER: _ClassVar[int]
    postal_address: str
    contact: str
    extra_info: str
    def __init__(self, postal_address: _Optional[str] = ..., contact: _Optional[str] = ..., extra_info: _Optional[str] = ...) -> None: ...

class PromptPayAccountPayload(_message.Message):
    __slots__ = ("prompt_pay_id",)
    PROMPT_PAY_ID_FIELD_NUMBER: _ClassVar[int]
    prompt_pay_id: str
    def __init__(self, prompt_pay_id: _Optional[str] = ...) -> None: ...

class AdvancedCashAccountPayload(_message.Message):
    __slots__ = ("account_nr",)
    ACCOUNT_NR_FIELD_NUMBER: _ClassVar[int]
    account_nr: str
    def __init__(self, account_nr: _Optional[str] = ...) -> None: ...

class TransferwiseAccountPayload(_message.Message):
    __slots__ = ("email",)
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    email: str
    def __init__(self, email: _Optional[str] = ...) -> None: ...

class TransferwiseUsdAccountPayload(_message.Message):
    __slots__ = ("email", "holder_name", "beneficiary_address")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    HOLDER_NAME_FIELD_NUMBER: _ClassVar[int]
    BENEFICIARY_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    email: str
    holder_name: str
    beneficiary_address: str
    def __init__(self, email: _Optional[str] = ..., holder_name: _Optional[str] = ..., beneficiary_address: _Optional[str] = ...) -> None: ...

class PayseraAccountPayload(_message.Message):
    __slots__ = ("email",)
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    email: str
    def __init__(self, email: _Optional[str] = ...) -> None: ...

class PaxumAccountPayload(_message.Message):
    __slots__ = ("email",)
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    email: str
    def __init__(self, email: _Optional[str] = ...) -> None: ...

class CapitualAccountPayload(_message.Message):
    __slots__ = ("account_nr",)
    ACCOUNT_NR_FIELD_NUMBER: _ClassVar[int]
    account_nr: str
    def __init__(self, account_nr: _Optional[str] = ...) -> None: ...

class CelPayAccountPayload(_message.Message):
    __slots__ = ("email",)
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    email: str
    def __init__(self, email: _Optional[str] = ...) -> None: ...

class NequiAccountPayload(_message.Message):
    __slots__ = ("mobile_nr",)
    MOBILE_NR_FIELD_NUMBER: _ClassVar[int]
    mobile_nr: str
    def __init__(self, mobile_nr: _Optional[str] = ...) -> None: ...

class BizumAccountPayload(_message.Message):
    __slots__ = ("mobile_nr",)
    MOBILE_NR_FIELD_NUMBER: _ClassVar[int]
    mobile_nr: str
    def __init__(self, mobile_nr: _Optional[str] = ...) -> None: ...

class PixAccountPayload(_message.Message):
    __slots__ = ("pix_key",)
    PIX_KEY_FIELD_NUMBER: _ClassVar[int]
    pix_key: str
    def __init__(self, pix_key: _Optional[str] = ...) -> None: ...

class MoneseAccountPayload(_message.Message):
    __slots__ = ("mobile_nr", "holder_name")
    MOBILE_NR_FIELD_NUMBER: _ClassVar[int]
    HOLDER_NAME_FIELD_NUMBER: _ClassVar[int]
    mobile_nr: str
    holder_name: str
    def __init__(self, mobile_nr: _Optional[str] = ..., holder_name: _Optional[str] = ...) -> None: ...

class SatispayAccountPayload(_message.Message):
    __slots__ = ("mobile_nr", "holder_name")
    MOBILE_NR_FIELD_NUMBER: _ClassVar[int]
    HOLDER_NAME_FIELD_NUMBER: _ClassVar[int]
    mobile_nr: str
    holder_name: str
    def __init__(self, mobile_nr: _Optional[str] = ..., holder_name: _Optional[str] = ...) -> None: ...

class StrikeAccountPayload(_message.Message):
    __slots__ = ("holder_name",)
    HOLDER_NAME_FIELD_NUMBER: _ClassVar[int]
    holder_name: str
    def __init__(self, holder_name: _Optional[str] = ...) -> None: ...

class TikkieAccountPayload(_message.Message):
    __slots__ = ("iban",)
    IBAN_FIELD_NUMBER: _ClassVar[int]
    iban: str
    def __init__(self, iban: _Optional[str] = ...) -> None: ...

class VerseAccountPayload(_message.Message):
    __slots__ = ("holder_name",)
    HOLDER_NAME_FIELD_NUMBER: _ClassVar[int]
    holder_name: str
    def __init__(self, holder_name: _Optional[str] = ...) -> None: ...

class MercadoPagoAccountPayload(_message.Message):
    __slots__ = ("holder_name", "holder_id")
    HOLDER_NAME_FIELD_NUMBER: _ClassVar[int]
    HOLDER_ID_FIELD_NUMBER: _ClassVar[int]
    holder_name: str
    holder_id: str
    def __init__(self, holder_name: _Optional[str] = ..., holder_id: _Optional[str] = ...) -> None: ...

class SwiftAccountPayload(_message.Message):
    __slots__ = ("beneficiary_name", "beneficiary_account_nr", "beneficiary_address", "beneficiary_city", "beneficiary_phone", "special_instructions", "bank_swift_code", "bank_country_code", "bank_name", "bank_branch", "bank_address", "intermediary_swift_code", "intermediary_country_code", "intermediary_name", "intermediary_branch", "intermediary_address")
    BENEFICIARY_NAME_FIELD_NUMBER: _ClassVar[int]
    BENEFICIARY_ACCOUNT_NR_FIELD_NUMBER: _ClassVar[int]
    BENEFICIARY_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    BENEFICIARY_CITY_FIELD_NUMBER: _ClassVar[int]
    BENEFICIARY_PHONE_FIELD_NUMBER: _ClassVar[int]
    SPECIAL_INSTRUCTIONS_FIELD_NUMBER: _ClassVar[int]
    BANK_SWIFT_CODE_FIELD_NUMBER: _ClassVar[int]
    BANK_COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    BANK_NAME_FIELD_NUMBER: _ClassVar[int]
    BANK_BRANCH_FIELD_NUMBER: _ClassVar[int]
    BANK_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    INTERMEDIARY_SWIFT_CODE_FIELD_NUMBER: _ClassVar[int]
    INTERMEDIARY_COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    INTERMEDIARY_NAME_FIELD_NUMBER: _ClassVar[int]
    INTERMEDIARY_BRANCH_FIELD_NUMBER: _ClassVar[int]
    INTERMEDIARY_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    beneficiary_name: str
    beneficiary_account_nr: str
    beneficiary_address: str
    beneficiary_city: str
    beneficiary_phone: str
    special_instructions: str
    bank_swift_code: str
    bank_country_code: str
    bank_name: str
    bank_branch: str
    bank_address: str
    intermediary_swift_code: str
    intermediary_country_code: str
    intermediary_name: str
    intermediary_branch: str
    intermediary_address: str
    def __init__(self, beneficiary_name: _Optional[str] = ..., beneficiary_account_nr: _Optional[str] = ..., beneficiary_address: _Optional[str] = ..., beneficiary_city: _Optional[str] = ..., beneficiary_phone: _Optional[str] = ..., special_instructions: _Optional[str] = ..., bank_swift_code: _Optional[str] = ..., bank_country_code: _Optional[str] = ..., bank_name: _Optional[str] = ..., bank_branch: _Optional[str] = ..., bank_address: _Optional[str] = ..., intermediary_swift_code: _Optional[str] = ..., intermediary_country_code: _Optional[str] = ..., intermediary_name: _Optional[str] = ..., intermediary_branch: _Optional[str] = ..., intermediary_address: _Optional[str] = ...) -> None: ...

class SbpAccountPayload(_message.Message):
    __slots__ = ("holder_name", "mobile_number", "bank_name")
    HOLDER_NAME_FIELD_NUMBER: _ClassVar[int]
    MOBILE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    BANK_NAME_FIELD_NUMBER: _ClassVar[int]
    holder_name: str
    mobile_number: str
    bank_name: str
    def __init__(self, holder_name: _Optional[str] = ..., mobile_number: _Optional[str] = ..., bank_name: _Optional[str] = ...) -> None: ...

class PersistableEnvelope(_message.Message):
    __slots__ = ("sequence_number_map", "persisted_entry_map", "peer_list", "address_entry_list", "navigation_path", "tradable_list", "arbitration_dispute_list", "preferences_payload", "user_payload", "payment_account_list", "account_age_witness_store", "trade_statistics2_store", "proposal_store", "temp_proposal_store", "blind_vote_store", "my_proposal_list", "ballot_list", "my_vote_list", "my_blind_vote_list", "dao_state_store", "my_reputation_list", "my_proof_of_burn_list", "unconfirmed_bsq_change_output_list", "signed_witness_store", "mediation_dispute_list", "refund_dispute_list", "trade_statistics3_store", "mailbox_message_list", "ignored_mailbox_map", "removed_payloads_map", "bsq_block_store", "burning_man_accounting_store")
    SEQUENCE_NUMBER_MAP_FIELD_NUMBER: _ClassVar[int]
    PERSISTED_ENTRY_MAP_FIELD_NUMBER: _ClassVar[int]
    PEER_LIST_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_ENTRY_LIST_FIELD_NUMBER: _ClassVar[int]
    NAVIGATION_PATH_FIELD_NUMBER: _ClassVar[int]
    TRADABLE_LIST_FIELD_NUMBER: _ClassVar[int]
    ARBITRATION_DISPUTE_LIST_FIELD_NUMBER: _ClassVar[int]
    PREFERENCES_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    USER_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_ACCOUNT_LIST_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_AGE_WITNESS_STORE_FIELD_NUMBER: _ClassVar[int]
    TRADE_STATISTICS2_STORE_FIELD_NUMBER: _ClassVar[int]
    PROPOSAL_STORE_FIELD_NUMBER: _ClassVar[int]
    TEMP_PROPOSAL_STORE_FIELD_NUMBER: _ClassVar[int]
    BLIND_VOTE_STORE_FIELD_NUMBER: _ClassVar[int]
    MY_PROPOSAL_LIST_FIELD_NUMBER: _ClassVar[int]
    BALLOT_LIST_FIELD_NUMBER: _ClassVar[int]
    MY_VOTE_LIST_FIELD_NUMBER: _ClassVar[int]
    MY_BLIND_VOTE_LIST_FIELD_NUMBER: _ClassVar[int]
    DAO_STATE_STORE_FIELD_NUMBER: _ClassVar[int]
    MY_REPUTATION_LIST_FIELD_NUMBER: _ClassVar[int]
    MY_PROOF_OF_BURN_LIST_FIELD_NUMBER: _ClassVar[int]
    UNCONFIRMED_BSQ_CHANGE_OUTPUT_LIST_FIELD_NUMBER: _ClassVar[int]
    SIGNED_WITNESS_STORE_FIELD_NUMBER: _ClassVar[int]
    MEDIATION_DISPUTE_LIST_FIELD_NUMBER: _ClassVar[int]
    REFUND_DISPUTE_LIST_FIELD_NUMBER: _ClassVar[int]
    TRADE_STATISTICS3_STORE_FIELD_NUMBER: _ClassVar[int]
    MAILBOX_MESSAGE_LIST_FIELD_NUMBER: _ClassVar[int]
    IGNORED_MAILBOX_MAP_FIELD_NUMBER: _ClassVar[int]
    REMOVED_PAYLOADS_MAP_FIELD_NUMBER: _ClassVar[int]
    BSQ_BLOCK_STORE_FIELD_NUMBER: _ClassVar[int]
    BURNING_MAN_ACCOUNTING_STORE_FIELD_NUMBER: _ClassVar[int]
    sequence_number_map: SequenceNumberMap
    persisted_entry_map: PersistedEntryMap
    peer_list: PeerList
    address_entry_list: AddressEntryList
    navigation_path: NavigationPath
    tradable_list: TradableList
    arbitration_dispute_list: ArbitrationDisputeList
    preferences_payload: PreferencesPayload
    user_payload: UserPayload
    payment_account_list: PaymentAccountList
    account_age_witness_store: AccountAgeWitnessStore
    trade_statistics2_store: TradeStatistics2Store
    proposal_store: ProposalStore
    temp_proposal_store: TempProposalStore
    blind_vote_store: BlindVoteStore
    my_proposal_list: MyProposalList
    ballot_list: BallotList
    my_vote_list: MyVoteList
    my_blind_vote_list: MyBlindVoteList
    dao_state_store: DaoStateStore
    my_reputation_list: MyReputationList
    my_proof_of_burn_list: MyProofOfBurnList
    unconfirmed_bsq_change_output_list: UnconfirmedBsqChangeOutputList
    signed_witness_store: SignedWitnessStore
    mediation_dispute_list: MediationDisputeList
    refund_dispute_list: RefundDisputeList
    trade_statistics3_store: TradeStatistics3Store
    mailbox_message_list: MailboxMessageList
    ignored_mailbox_map: IgnoredMailboxMap
    removed_payloads_map: RemovedPayloadsMap
    bsq_block_store: BsqBlockStore
    burning_man_accounting_store: BurningManAccountingStore
    def __init__(self, sequence_number_map: _Optional[_Union[SequenceNumberMap, _Mapping]] = ..., persisted_entry_map: _Optional[_Union[PersistedEntryMap, _Mapping]] = ..., peer_list: _Optional[_Union[PeerList, _Mapping]] = ..., address_entry_list: _Optional[_Union[AddressEntryList, _Mapping]] = ..., navigation_path: _Optional[_Union[NavigationPath, _Mapping]] = ..., tradable_list: _Optional[_Union[TradableList, _Mapping]] = ..., arbitration_dispute_list: _Optional[_Union[ArbitrationDisputeList, _Mapping]] = ..., preferences_payload: _Optional[_Union[PreferencesPayload, _Mapping]] = ..., user_payload: _Optional[_Union[UserPayload, _Mapping]] = ..., payment_account_list: _Optional[_Union[PaymentAccountList, _Mapping]] = ..., account_age_witness_store: _Optional[_Union[AccountAgeWitnessStore, _Mapping]] = ..., trade_statistics2_store: _Optional[_Union[TradeStatistics2Store, _Mapping]] = ..., proposal_store: _Optional[_Union[ProposalStore, _Mapping]] = ..., temp_proposal_store: _Optional[_Union[TempProposalStore, _Mapping]] = ..., blind_vote_store: _Optional[_Union[BlindVoteStore, _Mapping]] = ..., my_proposal_list: _Optional[_Union[MyProposalList, _Mapping]] = ..., ballot_list: _Optional[_Union[BallotList, _Mapping]] = ..., my_vote_list: _Optional[_Union[MyVoteList, _Mapping]] = ..., my_blind_vote_list: _Optional[_Union[MyBlindVoteList, _Mapping]] = ..., dao_state_store: _Optional[_Union[DaoStateStore, _Mapping]] = ..., my_reputation_list: _Optional[_Union[MyReputationList, _Mapping]] = ..., my_proof_of_burn_list: _Optional[_Union[MyProofOfBurnList, _Mapping]] = ..., unconfirmed_bsq_change_output_list: _Optional[_Union[UnconfirmedBsqChangeOutputList, _Mapping]] = ..., signed_witness_store: _Optional[_Union[SignedWitnessStore, _Mapping]] = ..., mediation_dispute_list: _Optional[_Union[MediationDisputeList, _Mapping]] = ..., refund_dispute_list: _Optional[_Union[RefundDisputeList, _Mapping]] = ..., trade_statistics3_store: _Optional[_Union[TradeStatistics3Store, _Mapping]] = ..., mailbox_message_list: _Optional[_Union[MailboxMessageList, _Mapping]] = ..., ignored_mailbox_map: _Optional[_Union[IgnoredMailboxMap, _Mapping]] = ..., removed_payloads_map: _Optional[_Union[RemovedPayloadsMap, _Mapping]] = ..., bsq_block_store: _Optional[_Union[BsqBlockStore, _Mapping]] = ..., burning_man_accounting_store: _Optional[_Union[BurningManAccountingStore, _Mapping]] = ...) -> None: ...

class SequenceNumberMap(_message.Message):
    __slots__ = ("sequence_number_entries",)
    SEQUENCE_NUMBER_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    sequence_number_entries: _containers.RepeatedCompositeFieldContainer[SequenceNumberEntry]
    def __init__(self, sequence_number_entries: _Optional[_Iterable[_Union[SequenceNumberEntry, _Mapping]]] = ...) -> None: ...

class SequenceNumberEntry(_message.Message):
    __slots__ = ("bytes", "map_value")
    BYTES_FIELD_NUMBER: _ClassVar[int]
    MAP_VALUE_FIELD_NUMBER: _ClassVar[int]
    bytes: ByteArray
    map_value: MapValue
    def __init__(self, bytes: _Optional[_Union[ByteArray, _Mapping]] = ..., map_value: _Optional[_Union[MapValue, _Mapping]] = ...) -> None: ...

class ByteArray(_message.Message):
    __slots__ = ("bytes",)
    BYTES_FIELD_NUMBER: _ClassVar[int]
    bytes: bytes
    def __init__(self, bytes: _Optional[bytes] = ...) -> None: ...

class MapValue(_message.Message):
    __slots__ = ("sequence_nr", "time_stamp")
    SEQUENCE_NR_FIELD_NUMBER: _ClassVar[int]
    TIME_STAMP_FIELD_NUMBER: _ClassVar[int]
    sequence_nr: int
    time_stamp: int
    def __init__(self, sequence_nr: _Optional[int] = ..., time_stamp: _Optional[int] = ...) -> None: ...

class PersistedEntryMap(_message.Message):
    __slots__ = ("persisted_entry_map",)
    class PersistedEntryMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ProtectedStorageEntry
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ProtectedStorageEntry, _Mapping]] = ...) -> None: ...
    PERSISTED_ENTRY_MAP_FIELD_NUMBER: _ClassVar[int]
    persisted_entry_map: _containers.MessageMap[str, ProtectedStorageEntry]
    def __init__(self, persisted_entry_map: _Optional[_Mapping[str, ProtectedStorageEntry]] = ...) -> None: ...

class AccountAgeWitnessStore(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[AccountAgeWitness]
    def __init__(self, items: _Optional[_Iterable[_Union[AccountAgeWitness, _Mapping]]] = ...) -> None: ...

class SignedWitnessStore(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[SignedWitness]
    def __init__(self, items: _Optional[_Iterable[_Union[SignedWitness, _Mapping]]] = ...) -> None: ...

class TradeStatistics2Store(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[TradeStatistics2]
    def __init__(self, items: _Optional[_Iterable[_Union[TradeStatistics2, _Mapping]]] = ...) -> None: ...

class TradeStatistics3Store(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[TradeStatistics3]
    def __init__(self, items: _Optional[_Iterable[_Union[TradeStatistics3, _Mapping]]] = ...) -> None: ...

class PeerList(_message.Message):
    __slots__ = ("peer",)
    PEER_FIELD_NUMBER: _ClassVar[int]
    peer: _containers.RepeatedCompositeFieldContainer[Peer]
    def __init__(self, peer: _Optional[_Iterable[_Union[Peer, _Mapping]]] = ...) -> None: ...

class AddressEntryList(_message.Message):
    __slots__ = ("address_entry",)
    ADDRESS_ENTRY_FIELD_NUMBER: _ClassVar[int]
    address_entry: _containers.RepeatedCompositeFieldContainer[AddressEntry]
    def __init__(self, address_entry: _Optional[_Iterable[_Union[AddressEntry, _Mapping]]] = ...) -> None: ...

class AddressEntry(_message.Message):
    __slots__ = ("offer_id", "context", "pub_key", "pub_key_hash", "coin_locked_in_multi_sig", "segwit")
    class Context(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PB_ERROR: _ClassVar[AddressEntry.Context]
        ARBITRATOR: _ClassVar[AddressEntry.Context]
        AVAILABLE: _ClassVar[AddressEntry.Context]
        OFFER_FUNDING: _ClassVar[AddressEntry.Context]
        RESERVED_FOR_TRADE: _ClassVar[AddressEntry.Context]
        MULTI_SIG: _ClassVar[AddressEntry.Context]
        TRADE_PAYOUT: _ClassVar[AddressEntry.Context]
    PB_ERROR: AddressEntry.Context
    ARBITRATOR: AddressEntry.Context
    AVAILABLE: AddressEntry.Context
    OFFER_FUNDING: AddressEntry.Context
    RESERVED_FOR_TRADE: AddressEntry.Context
    MULTI_SIG: AddressEntry.Context
    TRADE_PAYOUT: AddressEntry.Context
    OFFER_ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    PUB_KEY_FIELD_NUMBER: _ClassVar[int]
    PUB_KEY_HASH_FIELD_NUMBER: _ClassVar[int]
    COIN_LOCKED_IN_MULTI_SIG_FIELD_NUMBER: _ClassVar[int]
    SEGWIT_FIELD_NUMBER: _ClassVar[int]
    offer_id: str
    context: AddressEntry.Context
    pub_key: bytes
    pub_key_hash: bytes
    coin_locked_in_multi_sig: int
    segwit: bool
    def __init__(self, offer_id: _Optional[str] = ..., context: _Optional[_Union[AddressEntry.Context, str]] = ..., pub_key: _Optional[bytes] = ..., pub_key_hash: _Optional[bytes] = ..., coin_locked_in_multi_sig: _Optional[int] = ..., segwit: bool = ...) -> None: ...

class NavigationPath(_message.Message):
    __slots__ = ("path",)
    PATH_FIELD_NUMBER: _ClassVar[int]
    path: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, path: _Optional[_Iterable[str]] = ...) -> None: ...

class PaymentAccountList(_message.Message):
    __slots__ = ("payment_account",)
    PAYMENT_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    payment_account: _containers.RepeatedCompositeFieldContainer[PaymentAccount]
    def __init__(self, payment_account: _Optional[_Iterable[_Union[PaymentAccount, _Mapping]]] = ...) -> None: ...

class TradableList(_message.Message):
    __slots__ = ("tradable",)
    TRADABLE_FIELD_NUMBER: _ClassVar[int]
    tradable: _containers.RepeatedCompositeFieldContainer[Tradable]
    def __init__(self, tradable: _Optional[_Iterable[_Union[Tradable, _Mapping]]] = ...) -> None: ...

class Offer(_message.Message):
    __slots__ = ("offer_payload", "bsq_swap_offer_payload")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PB_ERROR: _ClassVar[Offer.State]
        UNKNOWN: _ClassVar[Offer.State]
        OFFER_FEE_PAID: _ClassVar[Offer.State]
        AVAILABLE: _ClassVar[Offer.State]
        NOT_AVAILABLE: _ClassVar[Offer.State]
        REMOVED: _ClassVar[Offer.State]
        MAKER_OFFLINE: _ClassVar[Offer.State]
    PB_ERROR: Offer.State
    UNKNOWN: Offer.State
    OFFER_FEE_PAID: Offer.State
    AVAILABLE: Offer.State
    NOT_AVAILABLE: Offer.State
    REMOVED: Offer.State
    MAKER_OFFLINE: Offer.State
    OFFER_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    BSQ_SWAP_OFFER_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    offer_payload: OfferPayload
    bsq_swap_offer_payload: BsqSwapOfferPayload
    def __init__(self, offer_payload: _Optional[_Union[OfferPayload, _Mapping]] = ..., bsq_swap_offer_payload: _Optional[_Union[BsqSwapOfferPayload, _Mapping]] = ...) -> None: ...

class OpenOffer(_message.Message):
    __slots__ = ("offer", "state", "arbitrator_node_address", "mediator_node_address", "refund_agent_node_address", "trigger_price")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PB_ERROR: _ClassVar[OpenOffer.State]
        AVAILABLE: _ClassVar[OpenOffer.State]
        RESERVED: _ClassVar[OpenOffer.State]
        CLOSED: _ClassVar[OpenOffer.State]
        CANCELED: _ClassVar[OpenOffer.State]
        DEACTIVATED: _ClassVar[OpenOffer.State]
    PB_ERROR: OpenOffer.State
    AVAILABLE: OpenOffer.State
    RESERVED: OpenOffer.State
    CLOSED: OpenOffer.State
    CANCELED: OpenOffer.State
    DEACTIVATED: OpenOffer.State
    OFFER_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ARBITRATOR_NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    MEDIATOR_NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    REFUND_AGENT_NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_PRICE_FIELD_NUMBER: _ClassVar[int]
    offer: Offer
    state: OpenOffer.State
    arbitrator_node_address: NodeAddress
    mediator_node_address: NodeAddress
    refund_agent_node_address: NodeAddress
    trigger_price: int
    def __init__(self, offer: _Optional[_Union[Offer, _Mapping]] = ..., state: _Optional[_Union[OpenOffer.State, str]] = ..., arbitrator_node_address: _Optional[_Union[NodeAddress, _Mapping]] = ..., mediator_node_address: _Optional[_Union[NodeAddress, _Mapping]] = ..., refund_agent_node_address: _Optional[_Union[NodeAddress, _Mapping]] = ..., trigger_price: _Optional[int] = ...) -> None: ...

class Tradable(_message.Message):
    __slots__ = ("open_offer", "buyer_as_maker_trade", "buyer_as_taker_trade", "seller_as_maker_trade", "seller_as_taker_trade", "bsq_swap_buyer_as_maker_trade", "bsq_swap_buyer_as_taker_trade", "bsq_swap_seller_as_maker_trade", "bsq_swap_seller_as_taker_trade")
    OPEN_OFFER_FIELD_NUMBER: _ClassVar[int]
    BUYER_AS_MAKER_TRADE_FIELD_NUMBER: _ClassVar[int]
    BUYER_AS_TAKER_TRADE_FIELD_NUMBER: _ClassVar[int]
    SELLER_AS_MAKER_TRADE_FIELD_NUMBER: _ClassVar[int]
    SELLER_AS_TAKER_TRADE_FIELD_NUMBER: _ClassVar[int]
    BSQ_SWAP_BUYER_AS_MAKER_TRADE_FIELD_NUMBER: _ClassVar[int]
    BSQ_SWAP_BUYER_AS_TAKER_TRADE_FIELD_NUMBER: _ClassVar[int]
    BSQ_SWAP_SELLER_AS_MAKER_TRADE_FIELD_NUMBER: _ClassVar[int]
    BSQ_SWAP_SELLER_AS_TAKER_TRADE_FIELD_NUMBER: _ClassVar[int]
    open_offer: OpenOffer
    buyer_as_maker_trade: BuyerAsMakerTrade
    buyer_as_taker_trade: BuyerAsTakerTrade
    seller_as_maker_trade: SellerAsMakerTrade
    seller_as_taker_trade: SellerAsTakerTrade
    bsq_swap_buyer_as_maker_trade: BsqSwapBuyerAsMakerTrade
    bsq_swap_buyer_as_taker_trade: BsqSwapBuyerAsTakerTrade
    bsq_swap_seller_as_maker_trade: BsqSwapSellerAsMakerTrade
    bsq_swap_seller_as_taker_trade: BsqSwapSellerAsTakerTrade
    def __init__(self, open_offer: _Optional[_Union[OpenOffer, _Mapping]] = ..., buyer_as_maker_trade: _Optional[_Union[BuyerAsMakerTrade, _Mapping]] = ..., buyer_as_taker_trade: _Optional[_Union[BuyerAsTakerTrade, _Mapping]] = ..., seller_as_maker_trade: _Optional[_Union[SellerAsMakerTrade, _Mapping]] = ..., seller_as_taker_trade: _Optional[_Union[SellerAsTakerTrade, _Mapping]] = ..., bsq_swap_buyer_as_maker_trade: _Optional[_Union[BsqSwapBuyerAsMakerTrade, _Mapping]] = ..., bsq_swap_buyer_as_taker_trade: _Optional[_Union[BsqSwapBuyerAsTakerTrade, _Mapping]] = ..., bsq_swap_seller_as_maker_trade: _Optional[_Union[BsqSwapSellerAsMakerTrade, _Mapping]] = ..., bsq_swap_seller_as_taker_trade: _Optional[_Union[BsqSwapSellerAsTakerTrade, _Mapping]] = ...) -> None: ...

class Trade(_message.Message):
    __slots__ = ("offer", "process_model", "taker_fee_tx_id", "deposit_tx_id", "payout_tx_id", "trade_amount_as_long", "tx_fee_as_long", "taker_fee_as_long", "take_offer_date", "is_currency_for_taker_fee_btc", "trade_price", "trading_peer_node_address", "state", "dispute_state", "trade_period_state", "contract", "contract_as_json", "contract_hash", "taker_contract_signature", "maker_contract_signature", "arbitrator_node_address", "mediator_node_address", "arbitrator_btc_pub_key", "taker_payment_account_id", "error_message", "arbitrator_pub_key_ring", "mediator_pub_key_ring", "counter_currency_tx_id", "chat_message", "mediation_result_state", "lock_time", "delayed_payout_tx_bytes", "refund_agent_node_address", "refund_agent_pub_key_ring", "refund_result_state", "last_refresh_request_date", "counter_currency_extra_data", "asset_tx_proof_result", "uid", "sellerConfirmedPaymentReceiptDate")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PB_ERROR_STATE: _ClassVar[Trade.State]
        PREPARATION: _ClassVar[Trade.State]
        TAKER_PUBLISHED_TAKER_FEE_TX: _ClassVar[Trade.State]
        MAKER_SENT_PUBLISH_DEPOSIT_TX_REQUEST: _ClassVar[Trade.State]
        MAKER_SAW_ARRIVED_PUBLISH_DEPOSIT_TX_REQUEST: _ClassVar[Trade.State]
        MAKER_STORED_IN_MAILBOX_PUBLISH_DEPOSIT_TX_REQUEST: _ClassVar[Trade.State]
        MAKER_SEND_FAILED_PUBLISH_DEPOSIT_TX_REQUEST: _ClassVar[Trade.State]
        TAKER_RECEIVED_PUBLISH_DEPOSIT_TX_REQUEST: _ClassVar[Trade.State]
        SELLER_PUBLISHED_DEPOSIT_TX: _ClassVar[Trade.State]
        SELLER_SENT_DEPOSIT_TX_PUBLISHED_MSG: _ClassVar[Trade.State]
        SELLER_SAW_ARRIVED_DEPOSIT_TX_PUBLISHED_MSG: _ClassVar[Trade.State]
        SELLER_STORED_IN_MAILBOX_DEPOSIT_TX_PUBLISHED_MSG: _ClassVar[Trade.State]
        SELLER_SEND_FAILED_DEPOSIT_TX_PUBLISHED_MSG: _ClassVar[Trade.State]
        BUYER_RECEIVED_DEPOSIT_TX_PUBLISHED_MSG: _ClassVar[Trade.State]
        BUYER_SAW_DEPOSIT_TX_IN_NETWORK: _ClassVar[Trade.State]
        DEPOSIT_CONFIRMED_IN_BLOCK_CHAIN: _ClassVar[Trade.State]
        BUYER_CONFIRMED_IN_UI_FIAT_PAYMENT_INITIATED: _ClassVar[Trade.State]
        BUYER_SENT_FIAT_PAYMENT_INITIATED_MSG: _ClassVar[Trade.State]
        BUYER_SAW_ARRIVED_FIAT_PAYMENT_INITIATED_MSG: _ClassVar[Trade.State]
        BUYER_STORED_IN_MAILBOX_FIAT_PAYMENT_INITIATED_MSG: _ClassVar[Trade.State]
        BUYER_SEND_FAILED_FIAT_PAYMENT_INITIATED_MSG: _ClassVar[Trade.State]
        SELLER_RECEIVED_FIAT_PAYMENT_INITIATED_MSG: _ClassVar[Trade.State]
        SELLER_CONFIRMED_IN_UI_FIAT_PAYMENT_RECEIPT: _ClassVar[Trade.State]
        SELLER_PUBLISHED_PAYOUT_TX: _ClassVar[Trade.State]
        SELLER_SENT_PAYOUT_TX_PUBLISHED_MSG: _ClassVar[Trade.State]
        SELLER_SAW_ARRIVED_PAYOUT_TX_PUBLISHED_MSG: _ClassVar[Trade.State]
        SELLER_STORED_IN_MAILBOX_PAYOUT_TX_PUBLISHED_MSG: _ClassVar[Trade.State]
        SELLER_SEND_FAILED_PAYOUT_TX_PUBLISHED_MSG: _ClassVar[Trade.State]
        BUYER_RECEIVED_PAYOUT_TX_PUBLISHED_MSG: _ClassVar[Trade.State]
        BUYER_SAW_PAYOUT_TX_IN_NETWORK: _ClassVar[Trade.State]
        WITHDRAW_COMPLETED: _ClassVar[Trade.State]
    PB_ERROR_STATE: Trade.State
    PREPARATION: Trade.State
    TAKER_PUBLISHED_TAKER_FEE_TX: Trade.State
    MAKER_SENT_PUBLISH_DEPOSIT_TX_REQUEST: Trade.State
    MAKER_SAW_ARRIVED_PUBLISH_DEPOSIT_TX_REQUEST: Trade.State
    MAKER_STORED_IN_MAILBOX_PUBLISH_DEPOSIT_TX_REQUEST: Trade.State
    MAKER_SEND_FAILED_PUBLISH_DEPOSIT_TX_REQUEST: Trade.State
    TAKER_RECEIVED_PUBLISH_DEPOSIT_TX_REQUEST: Trade.State
    SELLER_PUBLISHED_DEPOSIT_TX: Trade.State
    SELLER_SENT_DEPOSIT_TX_PUBLISHED_MSG: Trade.State
    SELLER_SAW_ARRIVED_DEPOSIT_TX_PUBLISHED_MSG: Trade.State
    SELLER_STORED_IN_MAILBOX_DEPOSIT_TX_PUBLISHED_MSG: Trade.State
    SELLER_SEND_FAILED_DEPOSIT_TX_PUBLISHED_MSG: Trade.State
    BUYER_RECEIVED_DEPOSIT_TX_PUBLISHED_MSG: Trade.State
    BUYER_SAW_DEPOSIT_TX_IN_NETWORK: Trade.State
    DEPOSIT_CONFIRMED_IN_BLOCK_CHAIN: Trade.State
    BUYER_CONFIRMED_IN_UI_FIAT_PAYMENT_INITIATED: Trade.State
    BUYER_SENT_FIAT_PAYMENT_INITIATED_MSG: Trade.State
    BUYER_SAW_ARRIVED_FIAT_PAYMENT_INITIATED_MSG: Trade.State
    BUYER_STORED_IN_MAILBOX_FIAT_PAYMENT_INITIATED_MSG: Trade.State
    BUYER_SEND_FAILED_FIAT_PAYMENT_INITIATED_MSG: Trade.State
    SELLER_RECEIVED_FIAT_PAYMENT_INITIATED_MSG: Trade.State
    SELLER_CONFIRMED_IN_UI_FIAT_PAYMENT_RECEIPT: Trade.State
    SELLER_PUBLISHED_PAYOUT_TX: Trade.State
    SELLER_SENT_PAYOUT_TX_PUBLISHED_MSG: Trade.State
    SELLER_SAW_ARRIVED_PAYOUT_TX_PUBLISHED_MSG: Trade.State
    SELLER_STORED_IN_MAILBOX_PAYOUT_TX_PUBLISHED_MSG: Trade.State
    SELLER_SEND_FAILED_PAYOUT_TX_PUBLISHED_MSG: Trade.State
    BUYER_RECEIVED_PAYOUT_TX_PUBLISHED_MSG: Trade.State
    BUYER_SAW_PAYOUT_TX_IN_NETWORK: Trade.State
    WITHDRAW_COMPLETED: Trade.State
    class Phase(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PB_ERROR_PHASE: _ClassVar[Trade.Phase]
        INIT: _ClassVar[Trade.Phase]
        TAKER_FEE_PUBLISHED: _ClassVar[Trade.Phase]
        DEPOSIT_PUBLISHED: _ClassVar[Trade.Phase]
        DEPOSIT_CONFIRMED: _ClassVar[Trade.Phase]
        FIAT_SENT: _ClassVar[Trade.Phase]
        FIAT_RECEIVED: _ClassVar[Trade.Phase]
        PAYOUT_PUBLISHED: _ClassVar[Trade.Phase]
        WITHDRAWN: _ClassVar[Trade.Phase]
    PB_ERROR_PHASE: Trade.Phase
    INIT: Trade.Phase
    TAKER_FEE_PUBLISHED: Trade.Phase
    DEPOSIT_PUBLISHED: Trade.Phase
    DEPOSIT_CONFIRMED: Trade.Phase
    FIAT_SENT: Trade.Phase
    FIAT_RECEIVED: Trade.Phase
    PAYOUT_PUBLISHED: Trade.Phase
    WITHDRAWN: Trade.Phase
    class DisputeState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PB_ERROR_DISPUTE_STATE: _ClassVar[Trade.DisputeState]
        NO_DISPUTE: _ClassVar[Trade.DisputeState]
        DISPUTE_REQUESTED: _ClassVar[Trade.DisputeState]
        DISPUTE_STARTED_BY_PEER: _ClassVar[Trade.DisputeState]
        DISPUTE_CLOSED: _ClassVar[Trade.DisputeState]
        MEDIATION_REQUESTED: _ClassVar[Trade.DisputeState]
        MEDIATION_STARTED_BY_PEER: _ClassVar[Trade.DisputeState]
        MEDIATION_CLOSED: _ClassVar[Trade.DisputeState]
        REFUND_REQUESTED: _ClassVar[Trade.DisputeState]
        REFUND_REQUEST_STARTED_BY_PEER: _ClassVar[Trade.DisputeState]
        REFUND_REQUEST_CLOSED: _ClassVar[Trade.DisputeState]
    PB_ERROR_DISPUTE_STATE: Trade.DisputeState
    NO_DISPUTE: Trade.DisputeState
    DISPUTE_REQUESTED: Trade.DisputeState
    DISPUTE_STARTED_BY_PEER: Trade.DisputeState
    DISPUTE_CLOSED: Trade.DisputeState
    MEDIATION_REQUESTED: Trade.DisputeState
    MEDIATION_STARTED_BY_PEER: Trade.DisputeState
    MEDIATION_CLOSED: Trade.DisputeState
    REFUND_REQUESTED: Trade.DisputeState
    REFUND_REQUEST_STARTED_BY_PEER: Trade.DisputeState
    REFUND_REQUEST_CLOSED: Trade.DisputeState
    class TradePeriodState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PB_ERROR_TRADE_PERIOD_STATE: _ClassVar[Trade.TradePeriodState]
        FIRST_HALF: _ClassVar[Trade.TradePeriodState]
        SECOND_HALF: _ClassVar[Trade.TradePeriodState]
        TRADE_PERIOD_OVER: _ClassVar[Trade.TradePeriodState]
    PB_ERROR_TRADE_PERIOD_STATE: Trade.TradePeriodState
    FIRST_HALF: Trade.TradePeriodState
    SECOND_HALF: Trade.TradePeriodState
    TRADE_PERIOD_OVER: Trade.TradePeriodState
    OFFER_FIELD_NUMBER: _ClassVar[int]
    PROCESS_MODEL_FIELD_NUMBER: _ClassVar[int]
    TAKER_FEE_TX_ID_FIELD_NUMBER: _ClassVar[int]
    DEPOSIT_TX_ID_FIELD_NUMBER: _ClassVar[int]
    PAYOUT_TX_ID_FIELD_NUMBER: _ClassVar[int]
    TRADE_AMOUNT_AS_LONG_FIELD_NUMBER: _ClassVar[int]
    TX_FEE_AS_LONG_FIELD_NUMBER: _ClassVar[int]
    TAKER_FEE_AS_LONG_FIELD_NUMBER: _ClassVar[int]
    TAKE_OFFER_DATE_FIELD_NUMBER: _ClassVar[int]
    IS_CURRENCY_FOR_TAKER_FEE_BTC_FIELD_NUMBER: _ClassVar[int]
    TRADE_PRICE_FIELD_NUMBER: _ClassVar[int]
    TRADING_PEER_NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    DISPUTE_STATE_FIELD_NUMBER: _ClassVar[int]
    TRADE_PERIOD_STATE_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_AS_JSON_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_HASH_FIELD_NUMBER: _ClassVar[int]
    TAKER_CONTRACT_SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    MAKER_CONTRACT_SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    ARBITRATOR_NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    MEDIATOR_NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    ARBITRATOR_BTC_PUB_KEY_FIELD_NUMBER: _ClassVar[int]
    TAKER_PAYMENT_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ARBITRATOR_PUB_KEY_RING_FIELD_NUMBER: _ClassVar[int]
    MEDIATOR_PUB_KEY_RING_FIELD_NUMBER: _ClassVar[int]
    COUNTER_CURRENCY_TX_ID_FIELD_NUMBER: _ClassVar[int]
    CHAT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    MEDIATION_RESULT_STATE_FIELD_NUMBER: _ClassVar[int]
    LOCK_TIME_FIELD_NUMBER: _ClassVar[int]
    DELAYED_PAYOUT_TX_BYTES_FIELD_NUMBER: _ClassVar[int]
    REFUND_AGENT_NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    REFUND_AGENT_PUB_KEY_RING_FIELD_NUMBER: _ClassVar[int]
    REFUND_RESULT_STATE_FIELD_NUMBER: _ClassVar[int]
    LAST_REFRESH_REQUEST_DATE_FIELD_NUMBER: _ClassVar[int]
    COUNTER_CURRENCY_EXTRA_DATA_FIELD_NUMBER: _ClassVar[int]
    ASSET_TX_PROOF_RESULT_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    SELLERCONFIRMEDPAYMENTRECEIPTDATE_FIELD_NUMBER: _ClassVar[int]
    offer: Offer
    process_model: ProcessModel
    taker_fee_tx_id: str
    deposit_tx_id: str
    payout_tx_id: str
    trade_amount_as_long: int
    tx_fee_as_long: int
    taker_fee_as_long: int
    take_offer_date: int
    is_currency_for_taker_fee_btc: bool
    trade_price: int
    trading_peer_node_address: NodeAddress
    state: Trade.State
    dispute_state: Trade.DisputeState
    trade_period_state: Trade.TradePeriodState
    contract: Contract
    contract_as_json: str
    contract_hash: bytes
    taker_contract_signature: str
    maker_contract_signature: str
    arbitrator_node_address: NodeAddress
    mediator_node_address: NodeAddress
    arbitrator_btc_pub_key: bytes
    taker_payment_account_id: str
    error_message: str
    arbitrator_pub_key_ring: PubKeyRing
    mediator_pub_key_ring: PubKeyRing
    counter_currency_tx_id: str
    chat_message: _containers.RepeatedCompositeFieldContainer[ChatMessage]
    mediation_result_state: MediationResultState
    lock_time: int
    delayed_payout_tx_bytes: bytes
    refund_agent_node_address: NodeAddress
    refund_agent_pub_key_ring: PubKeyRing
    refund_result_state: RefundResultState
    last_refresh_request_date: int
    counter_currency_extra_data: str
    asset_tx_proof_result: str
    uid: str
    sellerConfirmedPaymentReceiptDate: int
    def __init__(self, offer: _Optional[_Union[Offer, _Mapping]] = ..., process_model: _Optional[_Union[ProcessModel, _Mapping]] = ..., taker_fee_tx_id: _Optional[str] = ..., deposit_tx_id: _Optional[str] = ..., payout_tx_id: _Optional[str] = ..., trade_amount_as_long: _Optional[int] = ..., tx_fee_as_long: _Optional[int] = ..., taker_fee_as_long: _Optional[int] = ..., take_offer_date: _Optional[int] = ..., is_currency_for_taker_fee_btc: bool = ..., trade_price: _Optional[int] = ..., trading_peer_node_address: _Optional[_Union[NodeAddress, _Mapping]] = ..., state: _Optional[_Union[Trade.State, str]] = ..., dispute_state: _Optional[_Union[Trade.DisputeState, str]] = ..., trade_period_state: _Optional[_Union[Trade.TradePeriodState, str]] = ..., contract: _Optional[_Union[Contract, _Mapping]] = ..., contract_as_json: _Optional[str] = ..., contract_hash: _Optional[bytes] = ..., taker_contract_signature: _Optional[str] = ..., maker_contract_signature: _Optional[str] = ..., arbitrator_node_address: _Optional[_Union[NodeAddress, _Mapping]] = ..., mediator_node_address: _Optional[_Union[NodeAddress, _Mapping]] = ..., arbitrator_btc_pub_key: _Optional[bytes] = ..., taker_payment_account_id: _Optional[str] = ..., error_message: _Optional[str] = ..., arbitrator_pub_key_ring: _Optional[_Union[PubKeyRing, _Mapping]] = ..., mediator_pub_key_ring: _Optional[_Union[PubKeyRing, _Mapping]] = ..., counter_currency_tx_id: _Optional[str] = ..., chat_message: _Optional[_Iterable[_Union[ChatMessage, _Mapping]]] = ..., mediation_result_state: _Optional[_Union[MediationResultState, str]] = ..., lock_time: _Optional[int] = ..., delayed_payout_tx_bytes: _Optional[bytes] = ..., refund_agent_node_address: _Optional[_Union[NodeAddress, _Mapping]] = ..., refund_agent_pub_key_ring: _Optional[_Union[PubKeyRing, _Mapping]] = ..., refund_result_state: _Optional[_Union[RefundResultState, str]] = ..., last_refresh_request_date: _Optional[int] = ..., counter_currency_extra_data: _Optional[str] = ..., asset_tx_proof_result: _Optional[str] = ..., uid: _Optional[str] = ..., sellerConfirmedPaymentReceiptDate: _Optional[int] = ...) -> None: ...

class BuyerAsMakerTrade(_message.Message):
    __slots__ = ("trade",)
    TRADE_FIELD_NUMBER: _ClassVar[int]
    trade: Trade
    def __init__(self, trade: _Optional[_Union[Trade, _Mapping]] = ...) -> None: ...

class BuyerAsTakerTrade(_message.Message):
    __slots__ = ("trade",)
    TRADE_FIELD_NUMBER: _ClassVar[int]
    trade: Trade
    def __init__(self, trade: _Optional[_Union[Trade, _Mapping]] = ...) -> None: ...

class SellerAsMakerTrade(_message.Message):
    __slots__ = ("trade",)
    TRADE_FIELD_NUMBER: _ClassVar[int]
    trade: Trade
    def __init__(self, trade: _Optional[_Union[Trade, _Mapping]] = ...) -> None: ...

class SellerAsTakerTrade(_message.Message):
    __slots__ = ("trade",)
    TRADE_FIELD_NUMBER: _ClassVar[int]
    trade: Trade
    def __init__(self, trade: _Optional[_Union[Trade, _Mapping]] = ...) -> None: ...

class BsqSwapTrade(_message.Message):
    __slots__ = ("uid", "offer", "amount", "take_offer_date", "peer_node_address", "mining_fee_per_byte", "maker_fee", "taker_fee", "bsq_swap_protocol_model", "tx_id", "error_message", "state")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PB_ERROR_STATE: _ClassVar[BsqSwapTrade.State]
        PREPARATION: _ClassVar[BsqSwapTrade.State]
        COMPLETED: _ClassVar[BsqSwapTrade.State]
        FAILED: _ClassVar[BsqSwapTrade.State]
    PB_ERROR_STATE: BsqSwapTrade.State
    PREPARATION: BsqSwapTrade.State
    COMPLETED: BsqSwapTrade.State
    FAILED: BsqSwapTrade.State
    UID_FIELD_NUMBER: _ClassVar[int]
    OFFER_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    TAKE_OFFER_DATE_FIELD_NUMBER: _ClassVar[int]
    PEER_NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    MINING_FEE_PER_BYTE_FIELD_NUMBER: _ClassVar[int]
    MAKER_FEE_FIELD_NUMBER: _ClassVar[int]
    TAKER_FEE_FIELD_NUMBER: _ClassVar[int]
    BSQ_SWAP_PROTOCOL_MODEL_FIELD_NUMBER: _ClassVar[int]
    TX_ID_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    uid: str
    offer: Offer
    amount: int
    take_offer_date: int
    peer_node_address: NodeAddress
    mining_fee_per_byte: int
    maker_fee: int
    taker_fee: int
    bsq_swap_protocol_model: BsqSwapProtocolModel
    tx_id: str
    error_message: str
    state: BsqSwapTrade.State
    def __init__(self, uid: _Optional[str] = ..., offer: _Optional[_Union[Offer, _Mapping]] = ..., amount: _Optional[int] = ..., take_offer_date: _Optional[int] = ..., peer_node_address: _Optional[_Union[NodeAddress, _Mapping]] = ..., mining_fee_per_byte: _Optional[int] = ..., maker_fee: _Optional[int] = ..., taker_fee: _Optional[int] = ..., bsq_swap_protocol_model: _Optional[_Union[BsqSwapProtocolModel, _Mapping]] = ..., tx_id: _Optional[str] = ..., error_message: _Optional[str] = ..., state: _Optional[_Union[BsqSwapTrade.State, str]] = ...) -> None: ...

class BsqSwapBuyerAsMakerTrade(_message.Message):
    __slots__ = ("bsq_swap_trade",)
    BSQ_SWAP_TRADE_FIELD_NUMBER: _ClassVar[int]
    bsq_swap_trade: BsqSwapTrade
    def __init__(self, bsq_swap_trade: _Optional[_Union[BsqSwapTrade, _Mapping]] = ...) -> None: ...

class BsqSwapBuyerAsTakerTrade(_message.Message):
    __slots__ = ("bsq_swap_trade",)
    BSQ_SWAP_TRADE_FIELD_NUMBER: _ClassVar[int]
    bsq_swap_trade: BsqSwapTrade
    def __init__(self, bsq_swap_trade: _Optional[_Union[BsqSwapTrade, _Mapping]] = ...) -> None: ...

class BsqSwapSellerAsMakerTrade(_message.Message):
    __slots__ = ("bsq_swap_trade",)
    BSQ_SWAP_TRADE_FIELD_NUMBER: _ClassVar[int]
    bsq_swap_trade: BsqSwapTrade
    def __init__(self, bsq_swap_trade: _Optional[_Union[BsqSwapTrade, _Mapping]] = ...) -> None: ...

class BsqSwapSellerAsTakerTrade(_message.Message):
    __slots__ = ("bsq_swap_trade",)
    BSQ_SWAP_TRADE_FIELD_NUMBER: _ClassVar[int]
    bsq_swap_trade: BsqSwapTrade
    def __init__(self, bsq_swap_trade: _Optional[_Union[BsqSwapTrade, _Mapping]] = ...) -> None: ...

class ProcessModel(_message.Message):
    __slots__ = ("trading_peer", "offer_id", "account_id", "pub_key_ring", "take_offer_fee_tx_id", "payout_tx_signature", "prepared_deposit_tx", "raw_transaction_inputs", "change_output_value", "change_output_address", "use_savings_wallet", "funds_needed_for_trade_as_long", "my_multi_sig_pub_key", "temp_trading_peer_node_address", "payment_started_message_state", "mediated_payout_tx_signature", "buyer_payout_amount_from_mediation", "seller_payout_amount_from_mediation", "payment_account", "burning_man_selection_height")
    TRADING_PEER_FIELD_NUMBER: _ClassVar[int]
    OFFER_ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    PUB_KEY_RING_FIELD_NUMBER: _ClassVar[int]
    TAKE_OFFER_FEE_TX_ID_FIELD_NUMBER: _ClassVar[int]
    PAYOUT_TX_SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    PREPARED_DEPOSIT_TX_FIELD_NUMBER: _ClassVar[int]
    RAW_TRANSACTION_INPUTS_FIELD_NUMBER: _ClassVar[int]
    CHANGE_OUTPUT_VALUE_FIELD_NUMBER: _ClassVar[int]
    CHANGE_OUTPUT_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    USE_SAVINGS_WALLET_FIELD_NUMBER: _ClassVar[int]
    FUNDS_NEEDED_FOR_TRADE_AS_LONG_FIELD_NUMBER: _ClassVar[int]
    MY_MULTI_SIG_PUB_KEY_FIELD_NUMBER: _ClassVar[int]
    TEMP_TRADING_PEER_NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_STARTED_MESSAGE_STATE_FIELD_NUMBER: _ClassVar[int]
    MEDIATED_PAYOUT_TX_SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    BUYER_PAYOUT_AMOUNT_FROM_MEDIATION_FIELD_NUMBER: _ClassVar[int]
    SELLER_PAYOUT_AMOUNT_FROM_MEDIATION_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    BURNING_MAN_SELECTION_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    trading_peer: TradingPeer
    offer_id: str
    account_id: str
    pub_key_ring: PubKeyRing
    take_offer_fee_tx_id: str
    payout_tx_signature: bytes
    prepared_deposit_tx: bytes
    raw_transaction_inputs: _containers.RepeatedCompositeFieldContainer[RawTransactionInput]
    change_output_value: int
    change_output_address: str
    use_savings_wallet: bool
    funds_needed_for_trade_as_long: int
    my_multi_sig_pub_key: bytes
    temp_trading_peer_node_address: NodeAddress
    payment_started_message_state: str
    mediated_payout_tx_signature: bytes
    buyer_payout_amount_from_mediation: int
    seller_payout_amount_from_mediation: int
    payment_account: PaymentAccount
    burning_man_selection_height: int
    def __init__(self, trading_peer: _Optional[_Union[TradingPeer, _Mapping]] = ..., offer_id: _Optional[str] = ..., account_id: _Optional[str] = ..., pub_key_ring: _Optional[_Union[PubKeyRing, _Mapping]] = ..., take_offer_fee_tx_id: _Optional[str] = ..., payout_tx_signature: _Optional[bytes] = ..., prepared_deposit_tx: _Optional[bytes] = ..., raw_transaction_inputs: _Optional[_Iterable[_Union[RawTransactionInput, _Mapping]]] = ..., change_output_value: _Optional[int] = ..., change_output_address: _Optional[str] = ..., use_savings_wallet: bool = ..., funds_needed_for_trade_as_long: _Optional[int] = ..., my_multi_sig_pub_key: _Optional[bytes] = ..., temp_trading_peer_node_address: _Optional[_Union[NodeAddress, _Mapping]] = ..., payment_started_message_state: _Optional[str] = ..., mediated_payout_tx_signature: _Optional[bytes] = ..., buyer_payout_amount_from_mediation: _Optional[int] = ..., seller_payout_amount_from_mediation: _Optional[int] = ..., payment_account: _Optional[_Union[PaymentAccount, _Mapping]] = ..., burning_man_selection_height: _Optional[int] = ...) -> None: ...

class TradingPeer(_message.Message):
    __slots__ = ("account_id", "payment_account_payload", "payout_address_string", "contract_as_json", "contract_signature", "signature", "pub_key_ring", "multi_sig_pub_key", "raw_transaction_inputs", "change_output_value", "change_output_address", "account_age_witness_nonce", "account_age_witness_signature", "current_date", "mediated_payout_tx_signature", "hash_of_payment_account_payload")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_ACCOUNT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    PAYOUT_ADDRESS_STRING_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_AS_JSON_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    PUB_KEY_RING_FIELD_NUMBER: _ClassVar[int]
    MULTI_SIG_PUB_KEY_FIELD_NUMBER: _ClassVar[int]
    RAW_TRANSACTION_INPUTS_FIELD_NUMBER: _ClassVar[int]
    CHANGE_OUTPUT_VALUE_FIELD_NUMBER: _ClassVar[int]
    CHANGE_OUTPUT_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_AGE_WITNESS_NONCE_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_AGE_WITNESS_SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    CURRENT_DATE_FIELD_NUMBER: _ClassVar[int]
    MEDIATED_PAYOUT_TX_SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    HASH_OF_PAYMENT_ACCOUNT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    payment_account_payload: PaymentAccountPayload
    payout_address_string: str
    contract_as_json: str
    contract_signature: str
    signature: bytes
    pub_key_ring: PubKeyRing
    multi_sig_pub_key: bytes
    raw_transaction_inputs: _containers.RepeatedCompositeFieldContainer[RawTransactionInput]
    change_output_value: int
    change_output_address: str
    account_age_witness_nonce: bytes
    account_age_witness_signature: bytes
    current_date: int
    mediated_payout_tx_signature: bytes
    hash_of_payment_account_payload: bytes
    def __init__(self, account_id: _Optional[str] = ..., payment_account_payload: _Optional[_Union[PaymentAccountPayload, _Mapping]] = ..., payout_address_string: _Optional[str] = ..., contract_as_json: _Optional[str] = ..., contract_signature: _Optional[str] = ..., signature: _Optional[bytes] = ..., pub_key_ring: _Optional[_Union[PubKeyRing, _Mapping]] = ..., multi_sig_pub_key: _Optional[bytes] = ..., raw_transaction_inputs: _Optional[_Iterable[_Union[RawTransactionInput, _Mapping]]] = ..., change_output_value: _Optional[int] = ..., change_output_address: _Optional[str] = ..., account_age_witness_nonce: _Optional[bytes] = ..., account_age_witness_signature: _Optional[bytes] = ..., current_date: _Optional[int] = ..., mediated_payout_tx_signature: _Optional[bytes] = ..., hash_of_payment_account_payload: _Optional[bytes] = ...) -> None: ...

class BsqSwapProtocolModel(_message.Message):
    __slots__ = ("trade_peer", "pub_key_ring", "btc_address", "bsq_address", "inputs", "change", "payout", "tx", "tx_fee")
    TRADE_PEER_FIELD_NUMBER: _ClassVar[int]
    PUB_KEY_RING_FIELD_NUMBER: _ClassVar[int]
    BTC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    BSQ_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    INPUTS_FIELD_NUMBER: _ClassVar[int]
    CHANGE_FIELD_NUMBER: _ClassVar[int]
    PAYOUT_FIELD_NUMBER: _ClassVar[int]
    TX_FIELD_NUMBER: _ClassVar[int]
    TX_FEE_FIELD_NUMBER: _ClassVar[int]
    trade_peer: BsqSwapTradePeer
    pub_key_ring: PubKeyRing
    btc_address: str
    bsq_address: str
    inputs: _containers.RepeatedCompositeFieldContainer[RawTransactionInput]
    change: int
    payout: int
    tx: bytes
    tx_fee: int
    def __init__(self, trade_peer: _Optional[_Union[BsqSwapTradePeer, _Mapping]] = ..., pub_key_ring: _Optional[_Union[PubKeyRing, _Mapping]] = ..., btc_address: _Optional[str] = ..., bsq_address: _Optional[str] = ..., inputs: _Optional[_Iterable[_Union[RawTransactionInput, _Mapping]]] = ..., change: _Optional[int] = ..., payout: _Optional[int] = ..., tx: _Optional[bytes] = ..., tx_fee: _Optional[int] = ...) -> None: ...

class BsqSwapTradePeer(_message.Message):
    __slots__ = ("pub_key_ring", "btc_address", "bsq_address", "inputs", "change", "payout", "tx")
    PUB_KEY_RING_FIELD_NUMBER: _ClassVar[int]
    BTC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    BSQ_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    INPUTS_FIELD_NUMBER: _ClassVar[int]
    CHANGE_FIELD_NUMBER: _ClassVar[int]
    PAYOUT_FIELD_NUMBER: _ClassVar[int]
    TX_FIELD_NUMBER: _ClassVar[int]
    pub_key_ring: PubKeyRing
    btc_address: str
    bsq_address: str
    inputs: _containers.RepeatedCompositeFieldContainer[RawTransactionInput]
    change: int
    payout: int
    tx: bytes
    def __init__(self, pub_key_ring: _Optional[_Union[PubKeyRing, _Mapping]] = ..., btc_address: _Optional[str] = ..., bsq_address: _Optional[str] = ..., inputs: _Optional[_Iterable[_Union[RawTransactionInput, _Mapping]]] = ..., change: _Optional[int] = ..., payout: _Optional[int] = ..., tx: _Optional[bytes] = ...) -> None: ...

class ArbitrationDisputeList(_message.Message):
    __slots__ = ("dispute",)
    DISPUTE_FIELD_NUMBER: _ClassVar[int]
    dispute: _containers.RepeatedCompositeFieldContainer[Dispute]
    def __init__(self, dispute: _Optional[_Iterable[_Union[Dispute, _Mapping]]] = ...) -> None: ...

class MediationDisputeList(_message.Message):
    __slots__ = ("dispute",)
    DISPUTE_FIELD_NUMBER: _ClassVar[int]
    dispute: _containers.RepeatedCompositeFieldContainer[Dispute]
    def __init__(self, dispute: _Optional[_Iterable[_Union[Dispute, _Mapping]]] = ...) -> None: ...

class RefundDisputeList(_message.Message):
    __slots__ = ("dispute",)
    DISPUTE_FIELD_NUMBER: _ClassVar[int]
    dispute: _containers.RepeatedCompositeFieldContainer[Dispute]
    def __init__(self, dispute: _Optional[_Iterable[_Union[Dispute, _Mapping]]] = ...) -> None: ...

class PreferencesPayload(_message.Message):
    __slots__ = ("user_language", "user_country", "fiat_currencies", "crypto_currencies", "block_chain_explorer_main_net", "block_chain_explorer_test_net", "bsq_block_chain_explorer", "backup_directory", "auto_select_arbitrators", "dont_show_again_map", "tac_accepted", "use_tor_for_bitcoin_j", "show_own_offers_in_offer_book", "preferred_trade_currency", "withdrawal_tx_fee_in_vbytes", "use_custom_withdrawal_tx_fee", "max_price_distance_in_percent", "offer_book_chart_screen_currency_code", "trade_charts_screen_currency_code", "buy_screen_currency_code", "sell_screen_currency_code", "trade_statistics_tick_unit_index", "resync_Spv_requested", "sort_market_currencies_numerically", "use_percentage_based_price", "peer_tag_map", "bitcoin_nodes", "ignore_traders_list", "directory_chooser_path", "buyer_security_deposit_as_long", "use_animations", "selectedPayment_account_for_createOffer", "pay_fee_in_Btc", "bridge_addresses", "bridge_option_ordinal", "tor_transport_ordinal", "custom_bridges", "bitcoin_nodes_option_ordinal", "referral_id", "phone_key_and_token", "use_sound_for_mobile_notifications", "use_trade_notifications", "use_market_notifications", "use_price_notifications", "use_standby_mode", "is_dao_full_node", "rpc_user", "rpc_pw", "take_offer_selected_payment_account_id", "buyer_security_deposit_as_percent", "ignore_dust_threshold", "buyer_security_deposit_as_percent_for_crypto", "block_notify_port", "css_theme", "tac_accepted_v120", "auto_confirm_settings", "bsq_average_trim_threshold", "hide_non_account_payment_methods", "show_offers_matching_my_accounts", "deny_api_taker", "notify_on_pre_release", "use_full_mode_dao_monitor", "clear_data_after_days", "buy_screen_crypto_currency_code", "sell_screen_crypto_currency_code", "use_bitcoin_uris_in_qr_codes", "user_defined_trade_limit", "user_has_raised_trade_limit", "process_burning_man_accounting_data", "is_full_b_m_accounting_node", "use_bisq_wallet_funding")
    class DontShowAgainMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: bool
        def __init__(self, key: _Optional[str] = ..., value: bool = ...) -> None: ...
    class PeerTagMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    USER_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    USER_COUNTRY_FIELD_NUMBER: _ClassVar[int]
    FIAT_CURRENCIES_FIELD_NUMBER: _ClassVar[int]
    CRYPTO_CURRENCIES_FIELD_NUMBER: _ClassVar[int]
    BLOCK_CHAIN_EXPLORER_MAIN_NET_FIELD_NUMBER: _ClassVar[int]
    BLOCK_CHAIN_EXPLORER_TEST_NET_FIELD_NUMBER: _ClassVar[int]
    BSQ_BLOCK_CHAIN_EXPLORER_FIELD_NUMBER: _ClassVar[int]
    BACKUP_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    AUTO_SELECT_ARBITRATORS_FIELD_NUMBER: _ClassVar[int]
    DONT_SHOW_AGAIN_MAP_FIELD_NUMBER: _ClassVar[int]
    TAC_ACCEPTED_FIELD_NUMBER: _ClassVar[int]
    USE_TOR_FOR_BITCOIN_J_FIELD_NUMBER: _ClassVar[int]
    SHOW_OWN_OFFERS_IN_OFFER_BOOK_FIELD_NUMBER: _ClassVar[int]
    PREFERRED_TRADE_CURRENCY_FIELD_NUMBER: _ClassVar[int]
    WITHDRAWAL_TX_FEE_IN_VBYTES_FIELD_NUMBER: _ClassVar[int]
    USE_CUSTOM_WITHDRAWAL_TX_FEE_FIELD_NUMBER: _ClassVar[int]
    MAX_PRICE_DISTANCE_IN_PERCENT_FIELD_NUMBER: _ClassVar[int]
    OFFER_BOOK_CHART_SCREEN_CURRENCY_CODE_FIELD_NUMBER: _ClassVar[int]
    TRADE_CHARTS_SCREEN_CURRENCY_CODE_FIELD_NUMBER: _ClassVar[int]
    BUY_SCREEN_CURRENCY_CODE_FIELD_NUMBER: _ClassVar[int]
    SELL_SCREEN_CURRENCY_CODE_FIELD_NUMBER: _ClassVar[int]
    TRADE_STATISTICS_TICK_UNIT_INDEX_FIELD_NUMBER: _ClassVar[int]
    RESYNC_SPV_REQUESTED_FIELD_NUMBER: _ClassVar[int]
    SORT_MARKET_CURRENCIES_NUMERICALLY_FIELD_NUMBER: _ClassVar[int]
    USE_PERCENTAGE_BASED_PRICE_FIELD_NUMBER: _ClassVar[int]
    PEER_TAG_MAP_FIELD_NUMBER: _ClassVar[int]
    BITCOIN_NODES_FIELD_NUMBER: _ClassVar[int]
    IGNORE_TRADERS_LIST_FIELD_NUMBER: _ClassVar[int]
    DIRECTORY_CHOOSER_PATH_FIELD_NUMBER: _ClassVar[int]
    BUYER_SECURITY_DEPOSIT_AS_LONG_FIELD_NUMBER: _ClassVar[int]
    USE_ANIMATIONS_FIELD_NUMBER: _ClassVar[int]
    SELECTEDPAYMENT_ACCOUNT_FOR_CREATEOFFER_FIELD_NUMBER: _ClassVar[int]
    PAY_FEE_IN_BTC_FIELD_NUMBER: _ClassVar[int]
    BRIDGE_ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    BRIDGE_OPTION_ORDINAL_FIELD_NUMBER: _ClassVar[int]
    TOR_TRANSPORT_ORDINAL_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_BRIDGES_FIELD_NUMBER: _ClassVar[int]
    BITCOIN_NODES_OPTION_ORDINAL_FIELD_NUMBER: _ClassVar[int]
    REFERRAL_ID_FIELD_NUMBER: _ClassVar[int]
    PHONE_KEY_AND_TOKEN_FIELD_NUMBER: _ClassVar[int]
    USE_SOUND_FOR_MOBILE_NOTIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    USE_TRADE_NOTIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    USE_MARKET_NOTIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    USE_PRICE_NOTIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    USE_STANDBY_MODE_FIELD_NUMBER: _ClassVar[int]
    IS_DAO_FULL_NODE_FIELD_NUMBER: _ClassVar[int]
    RPC_USER_FIELD_NUMBER: _ClassVar[int]
    RPC_PW_FIELD_NUMBER: _ClassVar[int]
    TAKE_OFFER_SELECTED_PAYMENT_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    BUYER_SECURITY_DEPOSIT_AS_PERCENT_FIELD_NUMBER: _ClassVar[int]
    IGNORE_DUST_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    BUYER_SECURITY_DEPOSIT_AS_PERCENT_FOR_CRYPTO_FIELD_NUMBER: _ClassVar[int]
    BLOCK_NOTIFY_PORT_FIELD_NUMBER: _ClassVar[int]
    CSS_THEME_FIELD_NUMBER: _ClassVar[int]
    TAC_ACCEPTED_V120_FIELD_NUMBER: _ClassVar[int]
    AUTO_CONFIRM_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    BSQ_AVERAGE_TRIM_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    HIDE_NON_ACCOUNT_PAYMENT_METHODS_FIELD_NUMBER: _ClassVar[int]
    SHOW_OFFERS_MATCHING_MY_ACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    DENY_API_TAKER_FIELD_NUMBER: _ClassVar[int]
    NOTIFY_ON_PRE_RELEASE_FIELD_NUMBER: _ClassVar[int]
    USE_FULL_MODE_DAO_MONITOR_FIELD_NUMBER: _ClassVar[int]
    CLEAR_DATA_AFTER_DAYS_FIELD_NUMBER: _ClassVar[int]
    BUY_SCREEN_CRYPTO_CURRENCY_CODE_FIELD_NUMBER: _ClassVar[int]
    SELL_SCREEN_CRYPTO_CURRENCY_CODE_FIELD_NUMBER: _ClassVar[int]
    USE_BITCOIN_URIS_IN_QR_CODES_FIELD_NUMBER: _ClassVar[int]
    USER_DEFINED_TRADE_LIMIT_FIELD_NUMBER: _ClassVar[int]
    USER_HAS_RAISED_TRADE_LIMIT_FIELD_NUMBER: _ClassVar[int]
    PROCESS_BURNING_MAN_ACCOUNTING_DATA_FIELD_NUMBER: _ClassVar[int]
    IS_FULL_B_M_ACCOUNTING_NODE_FIELD_NUMBER: _ClassVar[int]
    USE_BISQ_WALLET_FUNDING_FIELD_NUMBER: _ClassVar[int]
    user_language: str
    user_country: Country
    fiat_currencies: _containers.RepeatedCompositeFieldContainer[TradeCurrency]
    crypto_currencies: _containers.RepeatedCompositeFieldContainer[TradeCurrency]
    block_chain_explorer_main_net: BlockChainExplorer
    block_chain_explorer_test_net: BlockChainExplorer
    bsq_block_chain_explorer: BlockChainExplorer
    backup_directory: str
    auto_select_arbitrators: bool
    dont_show_again_map: _containers.ScalarMap[str, bool]
    tac_accepted: bool
    use_tor_for_bitcoin_j: bool
    show_own_offers_in_offer_book: bool
    preferred_trade_currency: TradeCurrency
    withdrawal_tx_fee_in_vbytes: int
    use_custom_withdrawal_tx_fee: bool
    max_price_distance_in_percent: float
    offer_book_chart_screen_currency_code: str
    trade_charts_screen_currency_code: str
    buy_screen_currency_code: str
    sell_screen_currency_code: str
    trade_statistics_tick_unit_index: int
    resync_Spv_requested: bool
    sort_market_currencies_numerically: bool
    use_percentage_based_price: bool
    peer_tag_map: _containers.ScalarMap[str, str]
    bitcoin_nodes: str
    ignore_traders_list: _containers.RepeatedScalarFieldContainer[str]
    directory_chooser_path: str
    buyer_security_deposit_as_long: int
    use_animations: bool
    selectedPayment_account_for_createOffer: PaymentAccount
    pay_fee_in_Btc: bool
    bridge_addresses: _containers.RepeatedScalarFieldContainer[str]
    bridge_option_ordinal: int
    tor_transport_ordinal: int
    custom_bridges: str
    bitcoin_nodes_option_ordinal: int
    referral_id: str
    phone_key_and_token: str
    use_sound_for_mobile_notifications: bool
    use_trade_notifications: bool
    use_market_notifications: bool
    use_price_notifications: bool
    use_standby_mode: bool
    is_dao_full_node: bool
    rpc_user: str
    rpc_pw: str
    take_offer_selected_payment_account_id: str
    buyer_security_deposit_as_percent: float
    ignore_dust_threshold: int
    buyer_security_deposit_as_percent_for_crypto: float
    block_notify_port: int
    css_theme: int
    tac_accepted_v120: bool
    auto_confirm_settings: _containers.RepeatedCompositeFieldContainer[AutoConfirmSettings]
    bsq_average_trim_threshold: float
    hide_non_account_payment_methods: bool
    show_offers_matching_my_accounts: bool
    deny_api_taker: bool
    notify_on_pre_release: bool
    use_full_mode_dao_monitor: bool
    clear_data_after_days: int
    buy_screen_crypto_currency_code: str
    sell_screen_crypto_currency_code: str
    use_bitcoin_uris_in_qr_codes: bool
    user_defined_trade_limit: int
    user_has_raised_trade_limit: bool
    process_burning_man_accounting_data: bool
    is_full_b_m_accounting_node: bool
    use_bisq_wallet_funding: bool
    def __init__(self, user_language: _Optional[str] = ..., user_country: _Optional[_Union[Country, _Mapping]] = ..., fiat_currencies: _Optional[_Iterable[_Union[TradeCurrency, _Mapping]]] = ..., crypto_currencies: _Optional[_Iterable[_Union[TradeCurrency, _Mapping]]] = ..., block_chain_explorer_main_net: _Optional[_Union[BlockChainExplorer, _Mapping]] = ..., block_chain_explorer_test_net: _Optional[_Union[BlockChainExplorer, _Mapping]] = ..., bsq_block_chain_explorer: _Optional[_Union[BlockChainExplorer, _Mapping]] = ..., backup_directory: _Optional[str] = ..., auto_select_arbitrators: bool = ..., dont_show_again_map: _Optional[_Mapping[str, bool]] = ..., tac_accepted: bool = ..., use_tor_for_bitcoin_j: bool = ..., show_own_offers_in_offer_book: bool = ..., preferred_trade_currency: _Optional[_Union[TradeCurrency, _Mapping]] = ..., withdrawal_tx_fee_in_vbytes: _Optional[int] = ..., use_custom_withdrawal_tx_fee: bool = ..., max_price_distance_in_percent: _Optional[float] = ..., offer_book_chart_screen_currency_code: _Optional[str] = ..., trade_charts_screen_currency_code: _Optional[str] = ..., buy_screen_currency_code: _Optional[str] = ..., sell_screen_currency_code: _Optional[str] = ..., trade_statistics_tick_unit_index: _Optional[int] = ..., resync_Spv_requested: bool = ..., sort_market_currencies_numerically: bool = ..., use_percentage_based_price: bool = ..., peer_tag_map: _Optional[_Mapping[str, str]] = ..., bitcoin_nodes: _Optional[str] = ..., ignore_traders_list: _Optional[_Iterable[str]] = ..., directory_chooser_path: _Optional[str] = ..., buyer_security_deposit_as_long: _Optional[int] = ..., use_animations: bool = ..., selectedPayment_account_for_createOffer: _Optional[_Union[PaymentAccount, _Mapping]] = ..., pay_fee_in_Btc: bool = ..., bridge_addresses: _Optional[_Iterable[str]] = ..., bridge_option_ordinal: _Optional[int] = ..., tor_transport_ordinal: _Optional[int] = ..., custom_bridges: _Optional[str] = ..., bitcoin_nodes_option_ordinal: _Optional[int] = ..., referral_id: _Optional[str] = ..., phone_key_and_token: _Optional[str] = ..., use_sound_for_mobile_notifications: bool = ..., use_trade_notifications: bool = ..., use_market_notifications: bool = ..., use_price_notifications: bool = ..., use_standby_mode: bool = ..., is_dao_full_node: bool = ..., rpc_user: _Optional[str] = ..., rpc_pw: _Optional[str] = ..., take_offer_selected_payment_account_id: _Optional[str] = ..., buyer_security_deposit_as_percent: _Optional[float] = ..., ignore_dust_threshold: _Optional[int] = ..., buyer_security_deposit_as_percent_for_crypto: _Optional[float] = ..., block_notify_port: _Optional[int] = ..., css_theme: _Optional[int] = ..., tac_accepted_v120: bool = ..., auto_confirm_settings: _Optional[_Iterable[_Union[AutoConfirmSettings, _Mapping]]] = ..., bsq_average_trim_threshold: _Optional[float] = ..., hide_non_account_payment_methods: bool = ..., show_offers_matching_my_accounts: bool = ..., deny_api_taker: bool = ..., notify_on_pre_release: bool = ..., use_full_mode_dao_monitor: bool = ..., clear_data_after_days: _Optional[int] = ..., buy_screen_crypto_currency_code: _Optional[str] = ..., sell_screen_crypto_currency_code: _Optional[str] = ..., use_bitcoin_uris_in_qr_codes: bool = ..., user_defined_trade_limit: _Optional[int] = ..., user_has_raised_trade_limit: bool = ..., process_burning_man_accounting_data: bool = ..., is_full_b_m_accounting_node: bool = ..., use_bisq_wallet_funding: bool = ...) -> None: ...

class AutoConfirmSettings(_message.Message):
    __slots__ = ("enabled", "required_confirmations", "trade_limit", "service_addresses", "currency_code")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_CONFIRMATIONS_FIELD_NUMBER: _ClassVar[int]
    TRADE_LIMIT_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_CODE_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    required_confirmations: int
    trade_limit: int
    service_addresses: _containers.RepeatedScalarFieldContainer[str]
    currency_code: str
    def __init__(self, enabled: bool = ..., required_confirmations: _Optional[int] = ..., trade_limit: _Optional[int] = ..., service_addresses: _Optional[_Iterable[str]] = ..., currency_code: _Optional[str] = ...) -> None: ...

class UserPayload(_message.Message):
    __slots__ = ("account_id", "payment_accounts", "current_payment_account", "accepted_language_locale_codes", "developers_alert", "displayed_alert", "developers_filter", "accepted_arbitrators", "accepted_mediators", "registered_arbitrator", "registered_mediator", "price_alert_filter", "market_alert_filters", "accepted_refund_agents", "registered_refund_agent", "cookie", "sub_account_map_entries")
    class CookieEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_ACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    CURRENT_PAYMENT_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    ACCEPTED_LANGUAGE_LOCALE_CODES_FIELD_NUMBER: _ClassVar[int]
    DEVELOPERS_ALERT_FIELD_NUMBER: _ClassVar[int]
    DISPLAYED_ALERT_FIELD_NUMBER: _ClassVar[int]
    DEVELOPERS_FILTER_FIELD_NUMBER: _ClassVar[int]
    ACCEPTED_ARBITRATORS_FIELD_NUMBER: _ClassVar[int]
    ACCEPTED_MEDIATORS_FIELD_NUMBER: _ClassVar[int]
    REGISTERED_ARBITRATOR_FIELD_NUMBER: _ClassVar[int]
    REGISTERED_MEDIATOR_FIELD_NUMBER: _ClassVar[int]
    PRICE_ALERT_FILTER_FIELD_NUMBER: _ClassVar[int]
    MARKET_ALERT_FILTERS_FIELD_NUMBER: _ClassVar[int]
    ACCEPTED_REFUND_AGENTS_FIELD_NUMBER: _ClassVar[int]
    REGISTERED_REFUND_AGENT_FIELD_NUMBER: _ClassVar[int]
    COOKIE_FIELD_NUMBER: _ClassVar[int]
    SUB_ACCOUNT_MAP_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    payment_accounts: _containers.RepeatedCompositeFieldContainer[PaymentAccount]
    current_payment_account: PaymentAccount
    accepted_language_locale_codes: _containers.RepeatedScalarFieldContainer[str]
    developers_alert: Alert
    displayed_alert: Alert
    developers_filter: Filter
    accepted_arbitrators: _containers.RepeatedCompositeFieldContainer[Arbitrator]
    accepted_mediators: _containers.RepeatedCompositeFieldContainer[Mediator]
    registered_arbitrator: Arbitrator
    registered_mediator: Mediator
    price_alert_filter: PriceAlertFilter
    market_alert_filters: _containers.RepeatedCompositeFieldContainer[MarketAlertFilter]
    accepted_refund_agents: _containers.RepeatedCompositeFieldContainer[RefundAgent]
    registered_refund_agent: RefundAgent
    cookie: _containers.ScalarMap[str, str]
    sub_account_map_entries: _containers.RepeatedCompositeFieldContainer[SubAccountMapEntry]
    def __init__(self, account_id: _Optional[str] = ..., payment_accounts: _Optional[_Iterable[_Union[PaymentAccount, _Mapping]]] = ..., current_payment_account: _Optional[_Union[PaymentAccount, _Mapping]] = ..., accepted_language_locale_codes: _Optional[_Iterable[str]] = ..., developers_alert: _Optional[_Union[Alert, _Mapping]] = ..., displayed_alert: _Optional[_Union[Alert, _Mapping]] = ..., developers_filter: _Optional[_Union[Filter, _Mapping]] = ..., accepted_arbitrators: _Optional[_Iterable[_Union[Arbitrator, _Mapping]]] = ..., accepted_mediators: _Optional[_Iterable[_Union[Mediator, _Mapping]]] = ..., registered_arbitrator: _Optional[_Union[Arbitrator, _Mapping]] = ..., registered_mediator: _Optional[_Union[Mediator, _Mapping]] = ..., price_alert_filter: _Optional[_Union[PriceAlertFilter, _Mapping]] = ..., market_alert_filters: _Optional[_Iterable[_Union[MarketAlertFilter, _Mapping]]] = ..., accepted_refund_agents: _Optional[_Iterable[_Union[RefundAgent, _Mapping]]] = ..., registered_refund_agent: _Optional[_Union[RefundAgent, _Mapping]] = ..., cookie: _Optional[_Mapping[str, str]] = ..., sub_account_map_entries: _Optional[_Iterable[_Union[SubAccountMapEntry, _Mapping]]] = ...) -> None: ...

class SubAccountMapEntry(_message.Message):
    __slots__ = ("key", "value")
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: _containers.RepeatedCompositeFieldContainer[PaymentAccount]
    def __init__(self, key: _Optional[str] = ..., value: _Optional[_Iterable[_Union[PaymentAccount, _Mapping]]] = ...) -> None: ...

class AccountingTxOutput(_message.Message):
    __slots__ = ("value", "name")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    value: int
    name: str
    def __init__(self, value: _Optional[int] = ..., name: _Optional[str] = ...) -> None: ...

class AccountingTx(_message.Message):
    __slots__ = ("type", "outputs", "truncated_tx_id")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    OUTPUTS_FIELD_NUMBER: _ClassVar[int]
    TRUNCATED_TX_ID_FIELD_NUMBER: _ClassVar[int]
    type: int
    outputs: _containers.RepeatedCompositeFieldContainer[AccountingTxOutput]
    truncated_tx_id: bytes
    def __init__(self, type: _Optional[int] = ..., outputs: _Optional[_Iterable[_Union[AccountingTxOutput, _Mapping]]] = ..., truncated_tx_id: _Optional[bytes] = ...) -> None: ...

class AccountingBlock(_message.Message):
    __slots__ = ("height", "time_in_sec", "truncated_hash", "truncated_previous_block_hash", "txs")
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    TIME_IN_SEC_FIELD_NUMBER: _ClassVar[int]
    TRUNCATED_HASH_FIELD_NUMBER: _ClassVar[int]
    TRUNCATED_PREVIOUS_BLOCK_HASH_FIELD_NUMBER: _ClassVar[int]
    TXS_FIELD_NUMBER: _ClassVar[int]
    height: int
    time_in_sec: int
    truncated_hash: bytes
    truncated_previous_block_hash: bytes
    txs: _containers.RepeatedCompositeFieldContainer[AccountingTx]
    def __init__(self, height: _Optional[int] = ..., time_in_sec: _Optional[int] = ..., truncated_hash: _Optional[bytes] = ..., truncated_previous_block_hash: _Optional[bytes] = ..., txs: _Optional[_Iterable[_Union[AccountingTx, _Mapping]]] = ...) -> None: ...

class BurningManAccountingStore(_message.Message):
    __slots__ = ("blocks",)
    BLOCKS_FIELD_NUMBER: _ClassVar[int]
    blocks: _containers.RepeatedCompositeFieldContainer[AccountingBlock]
    def __init__(self, blocks: _Optional[_Iterable[_Union[AccountingBlock, _Mapping]]] = ...) -> None: ...

class GetAccountingBlocksRequest(_message.Message):
    __slots__ = ("from_block_height", "nonce", "sender_node_address", "supported_capabilities")
    FROM_BLOCK_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    NONCE_FIELD_NUMBER: _ClassVar[int]
    SENDER_NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    from_block_height: int
    nonce: int
    sender_node_address: NodeAddress
    supported_capabilities: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, from_block_height: _Optional[int] = ..., nonce: _Optional[int] = ..., sender_node_address: _Optional[_Union[NodeAddress, _Mapping]] = ..., supported_capabilities: _Optional[_Iterable[int]] = ...) -> None: ...

class GetAccountingBlocksResponse(_message.Message):
    __slots__ = ("blocks", "request_nonce", "pub_key", "signature")
    BLOCKS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_NONCE_FIELD_NUMBER: _ClassVar[int]
    PUB_KEY_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    blocks: _containers.RepeatedCompositeFieldContainer[AccountingBlock]
    request_nonce: int
    pub_key: str
    signature: bytes
    def __init__(self, blocks: _Optional[_Iterable[_Union[AccountingBlock, _Mapping]]] = ..., request_nonce: _Optional[int] = ..., pub_key: _Optional[str] = ..., signature: _Optional[bytes] = ...) -> None: ...

class NewAccountingBlockBroadcastMessage(_message.Message):
    __slots__ = ("block", "pub_key", "signature")
    BLOCK_FIELD_NUMBER: _ClassVar[int]
    PUB_KEY_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    block: AccountingBlock
    pub_key: str
    signature: bytes
    def __init__(self, block: _Optional[_Union[AccountingBlock, _Mapping]] = ..., pub_key: _Optional[str] = ..., signature: _Optional[bytes] = ...) -> None: ...

class BaseBlock(_message.Message):
    __slots__ = ("height", "time", "hash", "previous_block_hash", "raw_block", "block")
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_BLOCK_HASH_FIELD_NUMBER: _ClassVar[int]
    RAW_BLOCK_FIELD_NUMBER: _ClassVar[int]
    BLOCK_FIELD_NUMBER: _ClassVar[int]
    height: int
    time: int
    hash: str
    previous_block_hash: str
    raw_block: RawBlock
    block: Block
    def __init__(self, height: _Optional[int] = ..., time: _Optional[int] = ..., hash: _Optional[str] = ..., previous_block_hash: _Optional[str] = ..., raw_block: _Optional[_Union[RawBlock, _Mapping]] = ..., block: _Optional[_Union[Block, _Mapping]] = ...) -> None: ...

class BsqBlockStore(_message.Message):
    __slots__ = ("blocks",)
    BLOCKS_FIELD_NUMBER: _ClassVar[int]
    blocks: _containers.RepeatedCompositeFieldContainer[BaseBlock]
    def __init__(self, blocks: _Optional[_Iterable[_Union[BaseBlock, _Mapping]]] = ...) -> None: ...

class RawBlock(_message.Message):
    __slots__ = ("raw_txs",)
    RAW_TXS_FIELD_NUMBER: _ClassVar[int]
    raw_txs: _containers.RepeatedCompositeFieldContainer[BaseTx]
    def __init__(self, raw_txs: _Optional[_Iterable[_Union[BaseTx, _Mapping]]] = ...) -> None: ...

class Block(_message.Message):
    __slots__ = ("txs",)
    TXS_FIELD_NUMBER: _ClassVar[int]
    txs: _containers.RepeatedCompositeFieldContainer[BaseTx]
    def __init__(self, txs: _Optional[_Iterable[_Union[BaseTx, _Mapping]]] = ...) -> None: ...

class BaseTx(_message.Message):
    __slots__ = ("tx_version", "id", "block_height", "block_hash", "time", "tx_inputs", "raw_tx", "tx")
    TX_VERSION_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    BLOCK_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    BLOCK_HASH_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    TX_INPUTS_FIELD_NUMBER: _ClassVar[int]
    RAW_TX_FIELD_NUMBER: _ClassVar[int]
    TX_FIELD_NUMBER: _ClassVar[int]
    tx_version: str
    id: str
    block_height: int
    block_hash: str
    time: int
    tx_inputs: _containers.RepeatedCompositeFieldContainer[TxInput]
    raw_tx: RawTx
    tx: Tx
    def __init__(self, tx_version: _Optional[str] = ..., id: _Optional[str] = ..., block_height: _Optional[int] = ..., block_hash: _Optional[str] = ..., time: _Optional[int] = ..., tx_inputs: _Optional[_Iterable[_Union[TxInput, _Mapping]]] = ..., raw_tx: _Optional[_Union[RawTx, _Mapping]] = ..., tx: _Optional[_Union[Tx, _Mapping]] = ...) -> None: ...

class RawTx(_message.Message):
    __slots__ = ("raw_tx_outputs",)
    RAW_TX_OUTPUTS_FIELD_NUMBER: _ClassVar[int]
    raw_tx_outputs: _containers.RepeatedCompositeFieldContainer[BaseTxOutput]
    def __init__(self, raw_tx_outputs: _Optional[_Iterable[_Union[BaseTxOutput, _Mapping]]] = ...) -> None: ...

class Tx(_message.Message):
    __slots__ = ("tx_outputs", "txType", "burnt_bsq")
    TX_OUTPUTS_FIELD_NUMBER: _ClassVar[int]
    TXTYPE_FIELD_NUMBER: _ClassVar[int]
    BURNT_BSQ_FIELD_NUMBER: _ClassVar[int]
    tx_outputs: _containers.RepeatedCompositeFieldContainer[BaseTxOutput]
    txType: TxType
    burnt_bsq: int
    def __init__(self, tx_outputs: _Optional[_Iterable[_Union[BaseTxOutput, _Mapping]]] = ..., txType: _Optional[_Union[TxType, str]] = ..., burnt_bsq: _Optional[int] = ...) -> None: ...

class TxInput(_message.Message):
    __slots__ = ("connected_tx_output_tx_id", "connected_tx_output_index", "pub_key")
    CONNECTED_TX_OUTPUT_TX_ID_FIELD_NUMBER: _ClassVar[int]
    CONNECTED_TX_OUTPUT_INDEX_FIELD_NUMBER: _ClassVar[int]
    PUB_KEY_FIELD_NUMBER: _ClassVar[int]
    connected_tx_output_tx_id: str
    connected_tx_output_index: int
    pub_key: str
    def __init__(self, connected_tx_output_tx_id: _Optional[str] = ..., connected_tx_output_index: _Optional[int] = ..., pub_key: _Optional[str] = ...) -> None: ...

class BaseTxOutput(_message.Message):
    __slots__ = ("index", "value", "tx_id", "pub_key_script", "address", "op_return_data", "block_height", "raw_tx_output", "tx_output")
    INDEX_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    TX_ID_FIELD_NUMBER: _ClassVar[int]
    PUB_KEY_SCRIPT_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    OP_RETURN_DATA_FIELD_NUMBER: _ClassVar[int]
    BLOCK_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    RAW_TX_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    TX_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    index: int
    value: int
    tx_id: str
    pub_key_script: PubKeyScript
    address: str
    op_return_data: bytes
    block_height: int
    raw_tx_output: RawTxOutput
    tx_output: TxOutput
    def __init__(self, index: _Optional[int] = ..., value: _Optional[int] = ..., tx_id: _Optional[str] = ..., pub_key_script: _Optional[_Union[PubKeyScript, _Mapping]] = ..., address: _Optional[str] = ..., op_return_data: _Optional[bytes] = ..., block_height: _Optional[int] = ..., raw_tx_output: _Optional[_Union[RawTxOutput, _Mapping]] = ..., tx_output: _Optional[_Union[TxOutput, _Mapping]] = ...) -> None: ...

class UnconfirmedTxOutput(_message.Message):
    __slots__ = ("index", "value", "tx_id")
    INDEX_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    TX_ID_FIELD_NUMBER: _ClassVar[int]
    index: int
    value: int
    tx_id: str
    def __init__(self, index: _Optional[int] = ..., value: _Optional[int] = ..., tx_id: _Optional[str] = ...) -> None: ...

class RawTxOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TxOutput(_message.Message):
    __slots__ = ("tx_output_type", "lock_time", "unlock_block_height")
    TX_OUTPUT_TYPE_FIELD_NUMBER: _ClassVar[int]
    LOCK_TIME_FIELD_NUMBER: _ClassVar[int]
    UNLOCK_BLOCK_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    tx_output_type: TxOutputType
    lock_time: int
    unlock_block_height: int
    def __init__(self, tx_output_type: _Optional[_Union[TxOutputType, str]] = ..., lock_time: _Optional[int] = ..., unlock_block_height: _Optional[int] = ...) -> None: ...

class SpentInfo(_message.Message):
    __slots__ = ("block_height", "tx_id", "input_index")
    BLOCK_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    TX_ID_FIELD_NUMBER: _ClassVar[int]
    INPUT_INDEX_FIELD_NUMBER: _ClassVar[int]
    block_height: int
    tx_id: str
    input_index: int
    def __init__(self, block_height: _Optional[int] = ..., tx_id: _Optional[str] = ..., input_index: _Optional[int] = ...) -> None: ...

class PubKeyScript(_message.Message):
    __slots__ = ("req_sigs", "script_type", "addresses", "asm", "hex")
    REQ_SIGS_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_TYPE_FIELD_NUMBER: _ClassVar[int]
    ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    ASM_FIELD_NUMBER: _ClassVar[int]
    HEX_FIELD_NUMBER: _ClassVar[int]
    req_sigs: int
    script_type: ScriptType
    addresses: _containers.RepeatedScalarFieldContainer[str]
    asm: str
    hex: str
    def __init__(self, req_sigs: _Optional[int] = ..., script_type: _Optional[_Union[ScriptType, str]] = ..., addresses: _Optional[_Iterable[str]] = ..., asm: _Optional[str] = ..., hex: _Optional[str] = ...) -> None: ...

class DaoPhase(_message.Message):
    __slots__ = ("phase_ordinal", "duration")
    PHASE_ORDINAL_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    phase_ordinal: int
    duration: int
    def __init__(self, phase_ordinal: _Optional[int] = ..., duration: _Optional[int] = ...) -> None: ...

class Cycle(_message.Message):
    __slots__ = ("height_of_first_lock", "dao_phase")
    HEIGHT_OF_FIRST_LOCK_FIELD_NUMBER: _ClassVar[int]
    DAO_PHASE_FIELD_NUMBER: _ClassVar[int]
    height_of_first_lock: int
    dao_phase: _containers.RepeatedCompositeFieldContainer[DaoPhase]
    def __init__(self, height_of_first_lock: _Optional[int] = ..., dao_phase: _Optional[_Iterable[_Union[DaoPhase, _Mapping]]] = ...) -> None: ...

class DaoState(_message.Message):
    __slots__ = ("chain_height", "blocks", "cycles", "unspent_tx_output_map", "issuance_map", "confiscated_lockup_tx_list", "spent_info_map", "param_change_list", "evaluated_proposal_list", "decrypted_ballots_with_merits_list")
    class UnspentTxOutputMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: BaseTxOutput
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[BaseTxOutput, _Mapping]] = ...) -> None: ...
    class IssuanceMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Issuance
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Issuance, _Mapping]] = ...) -> None: ...
    class SpentInfoMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: SpentInfo
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[SpentInfo, _Mapping]] = ...) -> None: ...
    CHAIN_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    BLOCKS_FIELD_NUMBER: _ClassVar[int]
    CYCLES_FIELD_NUMBER: _ClassVar[int]
    UNSPENT_TX_OUTPUT_MAP_FIELD_NUMBER: _ClassVar[int]
    ISSUANCE_MAP_FIELD_NUMBER: _ClassVar[int]
    CONFISCATED_LOCKUP_TX_LIST_FIELD_NUMBER: _ClassVar[int]
    SPENT_INFO_MAP_FIELD_NUMBER: _ClassVar[int]
    PARAM_CHANGE_LIST_FIELD_NUMBER: _ClassVar[int]
    EVALUATED_PROPOSAL_LIST_FIELD_NUMBER: _ClassVar[int]
    DECRYPTED_BALLOTS_WITH_MERITS_LIST_FIELD_NUMBER: _ClassVar[int]
    chain_height: int
    blocks: _containers.RepeatedCompositeFieldContainer[BaseBlock]
    cycles: _containers.RepeatedCompositeFieldContainer[Cycle]
    unspent_tx_output_map: _containers.MessageMap[str, BaseTxOutput]
    issuance_map: _containers.MessageMap[str, Issuance]
    confiscated_lockup_tx_list: _containers.RepeatedScalarFieldContainer[str]
    spent_info_map: _containers.MessageMap[str, SpentInfo]
    param_change_list: _containers.RepeatedCompositeFieldContainer[ParamChange]
    evaluated_proposal_list: _containers.RepeatedCompositeFieldContainer[EvaluatedProposal]
    decrypted_ballots_with_merits_list: _containers.RepeatedCompositeFieldContainer[DecryptedBallotsWithMerits]
    def __init__(self, chain_height: _Optional[int] = ..., blocks: _Optional[_Iterable[_Union[BaseBlock, _Mapping]]] = ..., cycles: _Optional[_Iterable[_Union[Cycle, _Mapping]]] = ..., unspent_tx_output_map: _Optional[_Mapping[str, BaseTxOutput]] = ..., issuance_map: _Optional[_Mapping[str, Issuance]] = ..., confiscated_lockup_tx_list: _Optional[_Iterable[str]] = ..., spent_info_map: _Optional[_Mapping[str, SpentInfo]] = ..., param_change_list: _Optional[_Iterable[_Union[ParamChange, _Mapping]]] = ..., evaluated_proposal_list: _Optional[_Iterable[_Union[EvaluatedProposal, _Mapping]]] = ..., decrypted_ballots_with_merits_list: _Optional[_Iterable[_Union[DecryptedBallotsWithMerits, _Mapping]]] = ...) -> None: ...

class Issuance(_message.Message):
    __slots__ = ("tx_id", "chain_height", "amount", "pub_key", "issuance_type")
    TX_ID_FIELD_NUMBER: _ClassVar[int]
    CHAIN_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    PUB_KEY_FIELD_NUMBER: _ClassVar[int]
    ISSUANCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    tx_id: str
    chain_height: int
    amount: int
    pub_key: str
    issuance_type: str
    def __init__(self, tx_id: _Optional[str] = ..., chain_height: _Optional[int] = ..., amount: _Optional[int] = ..., pub_key: _Optional[str] = ..., issuance_type: _Optional[str] = ...) -> None: ...

class Proposal(_message.Message):
    __slots__ = ("name", "link", "version", "creation_date", "tx_id", "compensation_proposal", "reimbursement_proposal", "change_param_proposal", "role_proposal", "confiscate_bond_proposal", "generic_proposal", "remove_asset_proposal", "extra_data")
    class ExtraDataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    LINK_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    CREATION_DATE_FIELD_NUMBER: _ClassVar[int]
    TX_ID_FIELD_NUMBER: _ClassVar[int]
    COMPENSATION_PROPOSAL_FIELD_NUMBER: _ClassVar[int]
    REIMBURSEMENT_PROPOSAL_FIELD_NUMBER: _ClassVar[int]
    CHANGE_PARAM_PROPOSAL_FIELD_NUMBER: _ClassVar[int]
    ROLE_PROPOSAL_FIELD_NUMBER: _ClassVar[int]
    CONFISCATE_BOND_PROPOSAL_FIELD_NUMBER: _ClassVar[int]
    GENERIC_PROPOSAL_FIELD_NUMBER: _ClassVar[int]
    REMOVE_ASSET_PROPOSAL_FIELD_NUMBER: _ClassVar[int]
    EXTRA_DATA_FIELD_NUMBER: _ClassVar[int]
    name: str
    link: str
    version: int
    creation_date: int
    tx_id: str
    compensation_proposal: CompensationProposal
    reimbursement_proposal: ReimbursementProposal
    change_param_proposal: ChangeParamProposal
    role_proposal: RoleProposal
    confiscate_bond_proposal: ConfiscateBondProposal
    generic_proposal: GenericProposal
    remove_asset_proposal: RemoveAssetProposal
    extra_data: _containers.ScalarMap[str, str]
    def __init__(self, name: _Optional[str] = ..., link: _Optional[str] = ..., version: _Optional[int] = ..., creation_date: _Optional[int] = ..., tx_id: _Optional[str] = ..., compensation_proposal: _Optional[_Union[CompensationProposal, _Mapping]] = ..., reimbursement_proposal: _Optional[_Union[ReimbursementProposal, _Mapping]] = ..., change_param_proposal: _Optional[_Union[ChangeParamProposal, _Mapping]] = ..., role_proposal: _Optional[_Union[RoleProposal, _Mapping]] = ..., confiscate_bond_proposal: _Optional[_Union[ConfiscateBondProposal, _Mapping]] = ..., generic_proposal: _Optional[_Union[GenericProposal, _Mapping]] = ..., remove_asset_proposal: _Optional[_Union[RemoveAssetProposal, _Mapping]] = ..., extra_data: _Optional[_Mapping[str, str]] = ...) -> None: ...

class CompensationProposal(_message.Message):
    __slots__ = ("requested_bsq", "bsq_address")
    REQUESTED_BSQ_FIELD_NUMBER: _ClassVar[int]
    BSQ_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    requested_bsq: int
    bsq_address: str
    def __init__(self, requested_bsq: _Optional[int] = ..., bsq_address: _Optional[str] = ...) -> None: ...

class ReimbursementProposal(_message.Message):
    __slots__ = ("requested_bsq", "bsq_address")
    REQUESTED_BSQ_FIELD_NUMBER: _ClassVar[int]
    BSQ_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    requested_bsq: int
    bsq_address: str
    def __init__(self, requested_bsq: _Optional[int] = ..., bsq_address: _Optional[str] = ...) -> None: ...

class ChangeParamProposal(_message.Message):
    __slots__ = ("param", "param_value")
    PARAM_FIELD_NUMBER: _ClassVar[int]
    PARAM_VALUE_FIELD_NUMBER: _ClassVar[int]
    param: str
    param_value: str
    def __init__(self, param: _Optional[str] = ..., param_value: _Optional[str] = ...) -> None: ...

class RoleProposal(_message.Message):
    __slots__ = ("role", "required_bond_unit", "unlock_time")
    ROLE_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_BOND_UNIT_FIELD_NUMBER: _ClassVar[int]
    UNLOCK_TIME_FIELD_NUMBER: _ClassVar[int]
    role: Role
    required_bond_unit: int
    unlock_time: int
    def __init__(self, role: _Optional[_Union[Role, _Mapping]] = ..., required_bond_unit: _Optional[int] = ..., unlock_time: _Optional[int] = ...) -> None: ...

class ConfiscateBondProposal(_message.Message):
    __slots__ = ("lockup_tx_id",)
    LOCKUP_TX_ID_FIELD_NUMBER: _ClassVar[int]
    lockup_tx_id: str
    def __init__(self, lockup_tx_id: _Optional[str] = ...) -> None: ...

class GenericProposal(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RemoveAssetProposal(_message.Message):
    __slots__ = ("ticker_symbol",)
    TICKER_SYMBOL_FIELD_NUMBER: _ClassVar[int]
    ticker_symbol: str
    def __init__(self, ticker_symbol: _Optional[str] = ...) -> None: ...

class Role(_message.Message):
    __slots__ = ("uid", "name", "link", "bonded_role_type")
    UID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LINK_FIELD_NUMBER: _ClassVar[int]
    BONDED_ROLE_TYPE_FIELD_NUMBER: _ClassVar[int]
    uid: str
    name: str
    link: str
    bonded_role_type: str
    def __init__(self, uid: _Optional[str] = ..., name: _Optional[str] = ..., link: _Optional[str] = ..., bonded_role_type: _Optional[str] = ...) -> None: ...

class MyReputation(_message.Message):
    __slots__ = ("uid", "salt")
    UID_FIELD_NUMBER: _ClassVar[int]
    SALT_FIELD_NUMBER: _ClassVar[int]
    uid: str
    salt: bytes
    def __init__(self, uid: _Optional[str] = ..., salt: _Optional[bytes] = ...) -> None: ...

class MyReputationList(_message.Message):
    __slots__ = ("my_reputation",)
    MY_REPUTATION_FIELD_NUMBER: _ClassVar[int]
    my_reputation: _containers.RepeatedCompositeFieldContainer[MyReputation]
    def __init__(self, my_reputation: _Optional[_Iterable[_Union[MyReputation, _Mapping]]] = ...) -> None: ...

class MyProofOfBurn(_message.Message):
    __slots__ = ("tx_id", "pre_image")
    TX_ID_FIELD_NUMBER: _ClassVar[int]
    PRE_IMAGE_FIELD_NUMBER: _ClassVar[int]
    tx_id: str
    pre_image: str
    def __init__(self, tx_id: _Optional[str] = ..., pre_image: _Optional[str] = ...) -> None: ...

class MyProofOfBurnList(_message.Message):
    __slots__ = ("my_proof_of_burn",)
    MY_PROOF_OF_BURN_FIELD_NUMBER: _ClassVar[int]
    my_proof_of_burn: _containers.RepeatedCompositeFieldContainer[MyProofOfBurn]
    def __init__(self, my_proof_of_burn: _Optional[_Iterable[_Union[MyProofOfBurn, _Mapping]]] = ...) -> None: ...

class UnconfirmedBsqChangeOutputList(_message.Message):
    __slots__ = ("unconfirmed_tx_output",)
    UNCONFIRMED_TX_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    unconfirmed_tx_output: _containers.RepeatedCompositeFieldContainer[UnconfirmedTxOutput]
    def __init__(self, unconfirmed_tx_output: _Optional[_Iterable[_Union[UnconfirmedTxOutput, _Mapping]]] = ...) -> None: ...

class TempProposalPayload(_message.Message):
    __slots__ = ("proposal", "owner_pub_key_encoded", "extra_data")
    class ExtraDataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    PROPOSAL_FIELD_NUMBER: _ClassVar[int]
    OWNER_PUB_KEY_ENCODED_FIELD_NUMBER: _ClassVar[int]
    EXTRA_DATA_FIELD_NUMBER: _ClassVar[int]
    proposal: Proposal
    owner_pub_key_encoded: bytes
    extra_data: _containers.ScalarMap[str, str]
    def __init__(self, proposal: _Optional[_Union[Proposal, _Mapping]] = ..., owner_pub_key_encoded: _Optional[bytes] = ..., extra_data: _Optional[_Mapping[str, str]] = ...) -> None: ...

class ProposalPayload(_message.Message):
    __slots__ = ("proposal", "hash")
    PROPOSAL_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    proposal: Proposal
    hash: bytes
    def __init__(self, proposal: _Optional[_Union[Proposal, _Mapping]] = ..., hash: _Optional[bytes] = ...) -> None: ...

class ProposalStore(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[ProposalPayload]
    def __init__(self, items: _Optional[_Iterable[_Union[ProposalPayload, _Mapping]]] = ...) -> None: ...

class TempProposalStore(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[ProtectedStorageEntry]
    def __init__(self, items: _Optional[_Iterable[_Union[ProtectedStorageEntry, _Mapping]]] = ...) -> None: ...

class Ballot(_message.Message):
    __slots__ = ("proposal", "vote")
    PROPOSAL_FIELD_NUMBER: _ClassVar[int]
    VOTE_FIELD_NUMBER: _ClassVar[int]
    proposal: Proposal
    vote: Vote
    def __init__(self, proposal: _Optional[_Union[Proposal, _Mapping]] = ..., vote: _Optional[_Union[Vote, _Mapping]] = ...) -> None: ...

class MyProposalList(_message.Message):
    __slots__ = ("proposal",)
    PROPOSAL_FIELD_NUMBER: _ClassVar[int]
    proposal: _containers.RepeatedCompositeFieldContainer[Proposal]
    def __init__(self, proposal: _Optional[_Iterable[_Union[Proposal, _Mapping]]] = ...) -> None: ...

class BallotList(_message.Message):
    __slots__ = ("ballot",)
    BALLOT_FIELD_NUMBER: _ClassVar[int]
    ballot: _containers.RepeatedCompositeFieldContainer[Ballot]
    def __init__(self, ballot: _Optional[_Iterable[_Union[Ballot, _Mapping]]] = ...) -> None: ...

class ParamChange(_message.Message):
    __slots__ = ("param_name", "param_value", "activation_height")
    PARAM_NAME_FIELD_NUMBER: _ClassVar[int]
    PARAM_VALUE_FIELD_NUMBER: _ClassVar[int]
    ACTIVATION_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    param_name: str
    param_value: str
    activation_height: int
    def __init__(self, param_name: _Optional[str] = ..., param_value: _Optional[str] = ..., activation_height: _Optional[int] = ...) -> None: ...

class ConfiscateBond(_message.Message):
    __slots__ = ("lockup_tx_id",)
    LOCKUP_TX_ID_FIELD_NUMBER: _ClassVar[int]
    lockup_tx_id: str
    def __init__(self, lockup_tx_id: _Optional[str] = ...) -> None: ...

class MyVote(_message.Message):
    __slots__ = ("height", "ballot_list", "secret_key_encoded", "blind_vote", "date", "reveal_tx_id")
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    BALLOT_LIST_FIELD_NUMBER: _ClassVar[int]
    SECRET_KEY_ENCODED_FIELD_NUMBER: _ClassVar[int]
    BLIND_VOTE_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    REVEAL_TX_ID_FIELD_NUMBER: _ClassVar[int]
    height: int
    ballot_list: BallotList
    secret_key_encoded: bytes
    blind_vote: BlindVote
    date: int
    reveal_tx_id: str
    def __init__(self, height: _Optional[int] = ..., ballot_list: _Optional[_Union[BallotList, _Mapping]] = ..., secret_key_encoded: _Optional[bytes] = ..., blind_vote: _Optional[_Union[BlindVote, _Mapping]] = ..., date: _Optional[int] = ..., reveal_tx_id: _Optional[str] = ...) -> None: ...

class MyVoteList(_message.Message):
    __slots__ = ("my_vote",)
    MY_VOTE_FIELD_NUMBER: _ClassVar[int]
    my_vote: _containers.RepeatedCompositeFieldContainer[MyVote]
    def __init__(self, my_vote: _Optional[_Iterable[_Union[MyVote, _Mapping]]] = ...) -> None: ...

class VoteWithProposalTxId(_message.Message):
    __slots__ = ("proposal_tx_id", "vote")
    PROPOSAL_TX_ID_FIELD_NUMBER: _ClassVar[int]
    VOTE_FIELD_NUMBER: _ClassVar[int]
    proposal_tx_id: str
    vote: Vote
    def __init__(self, proposal_tx_id: _Optional[str] = ..., vote: _Optional[_Union[Vote, _Mapping]] = ...) -> None: ...

class VoteWithProposalTxIdList(_message.Message):
    __slots__ = ("item",)
    ITEM_FIELD_NUMBER: _ClassVar[int]
    item: _containers.RepeatedCompositeFieldContainer[VoteWithProposalTxId]
    def __init__(self, item: _Optional[_Iterable[_Union[VoteWithProposalTxId, _Mapping]]] = ...) -> None: ...

class BlindVote(_message.Message):
    __slots__ = ("encrypted_votes", "tx_id", "stake", "encrypted_merit_list", "date", "extra_data")
    class ExtraDataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ENCRYPTED_VOTES_FIELD_NUMBER: _ClassVar[int]
    TX_ID_FIELD_NUMBER: _ClassVar[int]
    STAKE_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_MERIT_LIST_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    EXTRA_DATA_FIELD_NUMBER: _ClassVar[int]
    encrypted_votes: bytes
    tx_id: str
    stake: int
    encrypted_merit_list: bytes
    date: int
    extra_data: _containers.ScalarMap[str, str]
    def __init__(self, encrypted_votes: _Optional[bytes] = ..., tx_id: _Optional[str] = ..., stake: _Optional[int] = ..., encrypted_merit_list: _Optional[bytes] = ..., date: _Optional[int] = ..., extra_data: _Optional[_Mapping[str, str]] = ...) -> None: ...

class MyBlindVoteList(_message.Message):
    __slots__ = ("blind_vote",)
    BLIND_VOTE_FIELD_NUMBER: _ClassVar[int]
    blind_vote: _containers.RepeatedCompositeFieldContainer[BlindVote]
    def __init__(self, blind_vote: _Optional[_Iterable[_Union[BlindVote, _Mapping]]] = ...) -> None: ...

class BlindVoteStore(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[BlindVotePayload]
    def __init__(self, items: _Optional[_Iterable[_Union[BlindVotePayload, _Mapping]]] = ...) -> None: ...

class BlindVotePayload(_message.Message):
    __slots__ = ("blind_vote", "hash")
    BLIND_VOTE_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    blind_vote: BlindVote
    hash: bytes
    def __init__(self, blind_vote: _Optional[_Union[BlindVote, _Mapping]] = ..., hash: _Optional[bytes] = ...) -> None: ...

class Vote(_message.Message):
    __slots__ = ("accepted",)
    ACCEPTED_FIELD_NUMBER: _ClassVar[int]
    accepted: bool
    def __init__(self, accepted: bool = ...) -> None: ...

class Merit(_message.Message):
    __slots__ = ("issuance", "signature")
    ISSUANCE_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    issuance: Issuance
    signature: bytes
    def __init__(self, issuance: _Optional[_Union[Issuance, _Mapping]] = ..., signature: _Optional[bytes] = ...) -> None: ...

class MeritList(_message.Message):
    __slots__ = ("merit",)
    MERIT_FIELD_NUMBER: _ClassVar[int]
    merit: _containers.RepeatedCompositeFieldContainer[Merit]
    def __init__(self, merit: _Optional[_Iterable[_Union[Merit, _Mapping]]] = ...) -> None: ...

class ProposalVoteResult(_message.Message):
    __slots__ = ("proposal", "stake_of_Accepted_votes", "stake_of_Rejected_votes", "num_accepted_votes", "num_rejected_votes", "num_ignored_votes")
    PROPOSAL_FIELD_NUMBER: _ClassVar[int]
    STAKE_OF_ACCEPTED_VOTES_FIELD_NUMBER: _ClassVar[int]
    STAKE_OF_REJECTED_VOTES_FIELD_NUMBER: _ClassVar[int]
    NUM_ACCEPTED_VOTES_FIELD_NUMBER: _ClassVar[int]
    NUM_REJECTED_VOTES_FIELD_NUMBER: _ClassVar[int]
    NUM_IGNORED_VOTES_FIELD_NUMBER: _ClassVar[int]
    proposal: Proposal
    stake_of_Accepted_votes: int
    stake_of_Rejected_votes: int
    num_accepted_votes: int
    num_rejected_votes: int
    num_ignored_votes: int
    def __init__(self, proposal: _Optional[_Union[Proposal, _Mapping]] = ..., stake_of_Accepted_votes: _Optional[int] = ..., stake_of_Rejected_votes: _Optional[int] = ..., num_accepted_votes: _Optional[int] = ..., num_rejected_votes: _Optional[int] = ..., num_ignored_votes: _Optional[int] = ...) -> None: ...

class EvaluatedProposal(_message.Message):
    __slots__ = ("is_accepted", "proposal_vote_result")
    IS_ACCEPTED_FIELD_NUMBER: _ClassVar[int]
    PROPOSAL_VOTE_RESULT_FIELD_NUMBER: _ClassVar[int]
    is_accepted: bool
    proposal_vote_result: ProposalVoteResult
    def __init__(self, is_accepted: bool = ..., proposal_vote_result: _Optional[_Union[ProposalVoteResult, _Mapping]] = ...) -> None: ...

class DecryptedBallotsWithMerits(_message.Message):
    __slots__ = ("hash_of_blind_vote_list", "blind_vote_tx_id", "vote_reveal_tx_id", "stake", "ballot_list", "merit_list")
    HASH_OF_BLIND_VOTE_LIST_FIELD_NUMBER: _ClassVar[int]
    BLIND_VOTE_TX_ID_FIELD_NUMBER: _ClassVar[int]
    VOTE_REVEAL_TX_ID_FIELD_NUMBER: _ClassVar[int]
    STAKE_FIELD_NUMBER: _ClassVar[int]
    BALLOT_LIST_FIELD_NUMBER: _ClassVar[int]
    MERIT_LIST_FIELD_NUMBER: _ClassVar[int]
    hash_of_blind_vote_list: bytes
    blind_vote_tx_id: str
    vote_reveal_tx_id: str
    stake: int
    ballot_list: BallotList
    merit_list: MeritList
    def __init__(self, hash_of_blind_vote_list: _Optional[bytes] = ..., blind_vote_tx_id: _Optional[str] = ..., vote_reveal_tx_id: _Optional[str] = ..., stake: _Optional[int] = ..., ballot_list: _Optional[_Union[BallotList, _Mapping]] = ..., merit_list: _Optional[_Union[MeritList, _Mapping]] = ...) -> None: ...

class DaoStateStore(_message.Message):
    __slots__ = ("dao_state", "dao_state_hash")
    DAO_STATE_FIELD_NUMBER: _ClassVar[int]
    DAO_STATE_HASH_FIELD_NUMBER: _ClassVar[int]
    dao_state: DaoState
    dao_state_hash: _containers.RepeatedCompositeFieldContainer[DaoStateHash]
    def __init__(self, dao_state: _Optional[_Union[DaoState, _Mapping]] = ..., dao_state_hash: _Optional[_Iterable[_Union[DaoStateHash, _Mapping]]] = ...) -> None: ...

class DaoStateHash(_message.Message):
    __slots__ = ("height", "hash", "prev_hash", "is_self_created")
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    PREV_HASH_FIELD_NUMBER: _ClassVar[int]
    IS_SELF_CREATED_FIELD_NUMBER: _ClassVar[int]
    height: int
    hash: bytes
    prev_hash: bytes
    is_self_created: bool
    def __init__(self, height: _Optional[int] = ..., hash: _Optional[bytes] = ..., prev_hash: _Optional[bytes] = ..., is_self_created: bool = ...) -> None: ...

class ProposalStateHash(_message.Message):
    __slots__ = ("height", "hash", "prev_hash", "num_proposals")
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    PREV_HASH_FIELD_NUMBER: _ClassVar[int]
    NUM_PROPOSALS_FIELD_NUMBER: _ClassVar[int]
    height: int
    hash: bytes
    prev_hash: bytes
    num_proposals: int
    def __init__(self, height: _Optional[int] = ..., hash: _Optional[bytes] = ..., prev_hash: _Optional[bytes] = ..., num_proposals: _Optional[int] = ...) -> None: ...

class BlindVoteStateHash(_message.Message):
    __slots__ = ("height", "hash", "prev_hash", "num_blind_votes")
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    PREV_HASH_FIELD_NUMBER: _ClassVar[int]
    NUM_BLIND_VOTES_FIELD_NUMBER: _ClassVar[int]
    height: int
    hash: bytes
    prev_hash: bytes
    num_blind_votes: int
    def __init__(self, height: _Optional[int] = ..., hash: _Optional[bytes] = ..., prev_hash: _Optional[bytes] = ..., num_blind_votes: _Optional[int] = ...) -> None: ...

class BlockChainExplorer(_message.Message):
    __slots__ = ("name", "tx_url", "address_url")
    NAME_FIELD_NUMBER: _ClassVar[int]
    TX_URL_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_URL_FIELD_NUMBER: _ClassVar[int]
    name: str
    tx_url: str
    address_url: str
    def __init__(self, name: _Optional[str] = ..., tx_url: _Optional[str] = ..., address_url: _Optional[str] = ...) -> None: ...

class PaymentAccount(_message.Message):
    __slots__ = ("id", "creation_date", "payment_method", "account_name", "trade_currencies", "selected_trade_currency", "payment_account_payload", "extra_data")
    class ExtraDataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    CREATION_DATE_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_METHOD_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_NAME_FIELD_NUMBER: _ClassVar[int]
    TRADE_CURRENCIES_FIELD_NUMBER: _ClassVar[int]
    SELECTED_TRADE_CURRENCY_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_ACCOUNT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    EXTRA_DATA_FIELD_NUMBER: _ClassVar[int]
    id: str
    creation_date: int
    payment_method: PaymentMethod
    account_name: str
    trade_currencies: _containers.RepeatedCompositeFieldContainer[TradeCurrency]
    selected_trade_currency: TradeCurrency
    payment_account_payload: PaymentAccountPayload
    extra_data: _containers.ScalarMap[str, str]
    def __init__(self, id: _Optional[str] = ..., creation_date: _Optional[int] = ..., payment_method: _Optional[_Union[PaymentMethod, _Mapping]] = ..., account_name: _Optional[str] = ..., trade_currencies: _Optional[_Iterable[_Union[TradeCurrency, _Mapping]]] = ..., selected_trade_currency: _Optional[_Union[TradeCurrency, _Mapping]] = ..., payment_account_payload: _Optional[_Union[PaymentAccountPayload, _Mapping]] = ..., extra_data: _Optional[_Mapping[str, str]] = ...) -> None: ...

class PaymentMethod(_message.Message):
    __slots__ = ("id", "max_trade_period", "max_trade_limit")
    ID_FIELD_NUMBER: _ClassVar[int]
    MAX_TRADE_PERIOD_FIELD_NUMBER: _ClassVar[int]
    MAX_TRADE_LIMIT_FIELD_NUMBER: _ClassVar[int]
    id: str
    max_trade_period: int
    max_trade_limit: int
    def __init__(self, id: _Optional[str] = ..., max_trade_period: _Optional[int] = ..., max_trade_limit: _Optional[int] = ...) -> None: ...

class Currency(_message.Message):
    __slots__ = ("currency_code",)
    CURRENCY_CODE_FIELD_NUMBER: _ClassVar[int]
    currency_code: str
    def __init__(self, currency_code: _Optional[str] = ...) -> None: ...

class TradeCurrency(_message.Message):
    __slots__ = ("code", "name", "crypto_currency", "fiat_currency")
    CODE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CRYPTO_CURRENCY_FIELD_NUMBER: _ClassVar[int]
    FIAT_CURRENCY_FIELD_NUMBER: _ClassVar[int]
    code: str
    name: str
    crypto_currency: CryptoCurrency
    fiat_currency: FiatCurrency
    def __init__(self, code: _Optional[str] = ..., name: _Optional[str] = ..., crypto_currency: _Optional[_Union[CryptoCurrency, _Mapping]] = ..., fiat_currency: _Optional[_Union[FiatCurrency, _Mapping]] = ...) -> None: ...

class CryptoCurrency(_message.Message):
    __slots__ = ("is_asset",)
    IS_ASSET_FIELD_NUMBER: _ClassVar[int]
    is_asset: bool
    def __init__(self, is_asset: bool = ...) -> None: ...

class FiatCurrency(_message.Message):
    __slots__ = ("currency",)
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    currency: Currency
    def __init__(self, currency: _Optional[_Union[Currency, _Mapping]] = ...) -> None: ...

class Country(_message.Message):
    __slots__ = ("code", "name", "region")
    CODE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    code: str
    name: str
    region: Region
    def __init__(self, code: _Optional[str] = ..., name: _Optional[str] = ..., region: _Optional[_Union[Region, _Mapping]] = ...) -> None: ...

class Region(_message.Message):
    __slots__ = ("code", "name")
    CODE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    code: str
    name: str
    def __init__(self, code: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class PriceAlertFilter(_message.Message):
    __slots__ = ("currencyCode", "high", "low")
    CURRENCYCODE_FIELD_NUMBER: _ClassVar[int]
    HIGH_FIELD_NUMBER: _ClassVar[int]
    LOW_FIELD_NUMBER: _ClassVar[int]
    currencyCode: str
    high: int
    low: int
    def __init__(self, currencyCode: _Optional[str] = ..., high: _Optional[int] = ..., low: _Optional[int] = ...) -> None: ...

class MarketAlertFilter(_message.Message):
    __slots__ = ("payment_account", "trigger_value", "is_buy_offer", "alert_ids")
    PAYMENT_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_VALUE_FIELD_NUMBER: _ClassVar[int]
    IS_BUY_OFFER_FIELD_NUMBER: _ClassVar[int]
    ALERT_IDS_FIELD_NUMBER: _ClassVar[int]
    payment_account: PaymentAccount
    trigger_value: int
    is_buy_offer: bool
    alert_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, payment_account: _Optional[_Union[PaymentAccount, _Mapping]] = ..., trigger_value: _Optional[int] = ..., is_buy_offer: bool = ..., alert_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class MockMailboxPayload(_message.Message):
    __slots__ = ("message", "sender_node_address", "uid")
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SENDER_NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    message: str
    sender_node_address: NodeAddress
    uid: str
    def __init__(self, message: _Optional[str] = ..., sender_node_address: _Optional[_Union[NodeAddress, _Mapping]] = ..., uid: _Optional[str] = ...) -> None: ...

class MockPayload(_message.Message):
    __slots__ = ("message_version", "message")
    MESSAGE_VERSION_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message_version: str
    message: str
    def __init__(self, message_version: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...

class ReportingItem(_message.Message):
    __slots__ = ("key", "group", "string_value_reporting_item", "long_value_reporting_item", "double_value_reporting_item")
    KEY_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    STRING_VALUE_REPORTING_ITEM_FIELD_NUMBER: _ClassVar[int]
    LONG_VALUE_REPORTING_ITEM_FIELD_NUMBER: _ClassVar[int]
    DOUBLE_VALUE_REPORTING_ITEM_FIELD_NUMBER: _ClassVar[int]
    key: str
    group: str
    string_value_reporting_item: StringValueReportingItem
    long_value_reporting_item: LongValueReportingItem
    double_value_reporting_item: DoubleValueReportingItem
    def __init__(self, key: _Optional[str] = ..., group: _Optional[str] = ..., string_value_reporting_item: _Optional[_Union[StringValueReportingItem, _Mapping]] = ..., long_value_reporting_item: _Optional[_Union[LongValueReportingItem, _Mapping]] = ..., double_value_reporting_item: _Optional[_Union[DoubleValueReportingItem, _Mapping]] = ...) -> None: ...

class StringValueReportingItem(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: str
    def __init__(self, value: _Optional[str] = ...) -> None: ...

class LongValueReportingItem(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: int
    def __init__(self, value: _Optional[int] = ...) -> None: ...

class DoubleValueReportingItem(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: float
    def __init__(self, value: _Optional[float] = ...) -> None: ...

class ReportingItems(_message.Message):
    __slots__ = ("address", "reporting_item")
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    REPORTING_ITEM_FIELD_NUMBER: _ClassVar[int]
    address: str
    reporting_item: _containers.RepeatedCompositeFieldContainer[ReportingItem]
    def __init__(self, address: _Optional[str] = ..., reporting_item: _Optional[_Iterable[_Union[ReportingItem, _Mapping]]] = ...) -> None: ...
