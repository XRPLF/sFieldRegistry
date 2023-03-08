
# SFCode Registry Tables

## How to use

1. If you are working on an Amendment to the XRP Ledger (or a sidechain) and you need additional serialized fields then you should register them here to avoid clobbering others.
2. Register by opening a PR against this repo with your proposed registration as changes to the tables below. Provided the reservations are reasonable these will be accepted.
3. If your code is already in use then enter it into the `used by` column otherwise use the `reserved by` column. Be descriptive but terse in the `reserved by` field. Other developers should understand why this code is being reserved.

## Bump Script

You can use the bump script if you already have the definitions file or a rippled build

python3 bump.py | action | name | path

- `python3 bump.py definitions Hooks ./definitions.json`
- `python3 bump.py rippled Hooks ./rippled`

> This will update the `README.md` and the `map.json` file.

## NOTPRESENT
Type 0

|Field Code|Field Name|Used by|Reserved by|
|-|-|-|-|


## UINT16
Type 1

|Field Code|Field Name|Used by|Reserved by|
|-|-|-|-|
|1|LedgerEntryType|Ledger|n/a|
|2|TransactionType|Transaction|n/a|
|3|SignerWeight|Transaction|n/a|
|4|TransferFee|Transaction|n/a|
|16|Version|n/a|n/a|
|17|HookStateChangeCount|Hooks|n/a|
|18|HookEmitCount|Hooks|n/a|
|19|HookExecutionIndex|Hooks|n/a|
|20|HookApiVersion|Hooks|n/a|


## UINT32
Type 2

|Field Code|Field Name|Used by|Reserved by|
|-|-|-|-|
|2|Flags|Transaction|n/a|
|3|SourceTag|Transaction|n/a|
|4|Sequence|Transaction|n/a|
|5|PreviousTxnLgrSeq|Transaction|n/a|
|6|LedgerSequence|Transaction|n/a|
|7|CloseTime|Ledger|n/a|
|8|ParentCloseTime|Ledger|n/a|
|9|SigningTime|Transaction|n/a|
|10|Expiration|AccountSet|n/a|
|11|TransferRate|AccountSet|n/a|
|12|WalletSize|AccountSet|n/a|
|13|OwnerCount|AccountSet|n/a|
|14|DestinationTag|Payment|n/a|
|16|HighQualityIn|Trustlines|n/a|
|17|HighQualityOut|Trustlines|n/a|
|18|LowQualityIn|Trustlines|n/a|
|19|LowQualityOut|Trustlines|n/a|
|20|QualityIn|Trustlines|n/a|
|21|QualityOut|Trustlines|n/a|
|22|StampEscrow|legacy/unused|n/a|
|23|BondAmount|legacy/unused|n/a|
|24|LoadFee|Consensus|n/a|
|25|OfferSequence|OfferCreate|n/a|
|26|FirstLedgerSequence|negativeUNL|n/a|
|27|LastLedgerSequence|All Txns|n/a|
|28|TransactionIndex|Metadata|n/a|
|29|OperationLimit|legacy/unused|n/a|
|30|ReferenceFeeUnits|FeeSettings|n/a|
|31|ReserveBase|FeeSettings|n/a|
|32|ReserveIncrement|FeeSettings|n/a|
|33|SetFlag|AccountSet|n/a|
|34|ClearFlag|AccountSet|n/a|
|35|SignerQuorum|MultiSign|n/a|
|36|CancelAfter|Escrow, Paychan|n/a|
|37|FinishAfter|Escrow, Paychan|n/a|
|38|SignerListID|Multisign|n/a|
|39|SettleDelay|Paychans|n/a|
|40|TicketCount|Tickets|n/a|
|41|TicketSequence|Tickets|n/a|
|42|NFTokenTaxon|XLS20|n/a|
|43|MintedNFTokens|XLS20|n/a|
|44|BurnedNFTokens|XLS20|n/a|
|45|HookStateCount|Hooks|n/a|
|46|EmitGeneration|Hooks|n/a|


## UINT64
Type 3

|Field Code|Field Name|Used by|Reserved by|
|-|-|-|-|
|1|IndexNext|Directories|n/a|
|2|IndexPrevious|Directories|n/a|
|3|BookNode|Orderbooks|n/a|
|4|OwnerNode|Directories|n/a|
|5|BaseFee|FeeSettings|n/a|
|6|ExchangeRate|Orderbooks|n/a|
|7|LowNode|Checks|n/a|
|8|HighNode|Checks|n/a|
|9|DestinationNode|Checks, Escrow, Paychan|n/a|
|10|Cookie|Validations|n/a|
|11|ServerVersion|Validations|n/a|
|12|NFTokenOfferNode|XLS20|n/a|
|13|EmitBurden|Hooks|n/a|
|16|HookOn|Hooks|n/a|
|17|HookInstructionCount|Hooks|n/a|
|18|HookReturnCode|Hooks|n/a|
|19|ReferenceCount|Hooks|n/a|


## HASH128
Type 4

|Field Code|Field Name|Used by|Reserved by|
|-|-|-|-|
|1|EmailHash|AccountSet|n/a|


## HASH256
Type 5

|Field Code|Field Name|Used by|Reserved by|
|-|-|-|-|
|1|LedgerHash|Metadata|n/a|
|2|ParentHash|Metadata|n/a|
|3|TransactionHash|Metadata|n/a|
|4|AccountHash|AccountSet|n/a|
|5|PreviousTxnID|Various|n/a|
|6|LedgerIndex|Metadata|n/a|
|7|WalletLocator|AccountSet|n/a|
|8|RootIndex|Directories|n/a|
|9|AccountTxnID|Account Root|n/a|
|10|NFTokenID|XLS20|n/a|
|11|EmitParentTxnID|Hooks|n/a|
|12|EmitNonce|Hooks|n/a|
|13|EmitHookHash|Hooks|n/a|
|16|BookDirectory|Directories|n/a|
|17|InvoiceID|Payment, Check|n/a|
|18|Nickname|legacy/unused|n/a|
|19|Amendment|Consensus|n/a|
|21|Digest|XLS35|n/a|
|22|Channel|Paychan|n/a|
|23|ConsensusHash|Consensus|n/a|
|24|CheckID|Hooks|n/a|
|25|ValidatedHash|Consensus|n/a|
|26|PreviousPageMin|XLS20|n/a|
|27|NextPageMin|XLS20|n/a|
|28|NFTokenBuyOffer|XLS20|n/a|
|29|NFTokenSellOffer|XLS20|n/a|
|30|HookStateKey|Hooks|n/a|
|31|HookHash|Hooks|n/a|
|32|HookNamespace|Hooks|n/a|
|33|HookSetTxnID|Hooks|n/a|
|257|hash|v1.10.0|n/a|
|258|index|v1.10.0|n/a|


## AMOUNT
Type 6

|Field Code|Field Name|Used by|Reserved by|
|-|-|-|-|
|1|Amount|Payment, TrustSet|n/a|
|2|Balance|Account Root, Paychan|n/a|
|3|LimitAmount|TrustSet|n/a|
|4|TakerPays|OfferCreate|n/a|
|5|TakerGets|OfferCreate|n/a|
|6|LowLimit|TrustSet|n/a|
|7|HighLimit|TrustSet|n/a|
|8|Fee|All Txns|n/a|
|9|SendMax|Partial payments|n/a|
|10|DeliverMin|Partial payments|n/a|
|16|MinimumOffer|legacy/unused|n/a|
|17|RippleEscrow|legacy/unused|n/a|
|18|DeliveredAmount|Partial payments|n/a|
|19|NFTokenBrokerFee|XLS20|n/a|
|22|BaseFeeDrops|FeeSettings|n/a|
|23|ReserveBaseDrops|FeeSettings|n/a|
|24|ReserveIncrementDrops|FeeSettings|n/a|
|258|taker_gets_funded|v1.10.0|n/a|
|259|taker_pays_funded|v1.10.0|n/a|


## BLOB
Type 7

|Field Code|Field Name|Used by|Reserved by|
|-|-|-|-|
|1|PublicKey|All Txns|n/a|
|2|MessageKey|AccountRoot|n/a|
|3|SigningPubKey|Transactions|n/a|
|4|TxnSignature|Transactions|n/a|
|5|URI|XLS20, XLS35|n/a|
|6|Signature|Validations|n/a|
|7|Domain|AccountRoot|n/a|
|8|FundCode|Legacy/unused|n/a|
|9|RemoveCode|Legacy/unused|n/a|
|10|ExpireCode|Legacy/unused|n/a|
|11|CreateCode|Hooks|n/a|
|12|MemoType|All Txns|n/a|
|13|MemoData|All Txns|n/a|
|14|MemoFormat|All Txns|n/a|
|16|Fulfillment|EscrowCreate|n/a|
|17|Condition|EscrowCreate|n/a|
|18|MasterSignature|ValidatorList|n/a|
|19|UNLModifyValidator|negativeUNL|n/a|
|20|ValidatorToDisable|negativeUNL|n/a|
|21|ValidatorToReEnable|negativeUNL|n/a|
|22|HookStateData|Hooks|n/a|
|23|HookReturnString|Hooks|n/a|
|24|HookParameterName|Hooks|n/a|
|25|HookParameterValue|Hooks|n/a|


## ACCOUNTID
Type 8

|Field Code|Field Name|Used by|Reserved by|
|-|-|-|-|
|1|Account|Various|n/a|
|2|Owner|XLS20|n/a|
|3|Destination|Payment|n/a|
|4|Issuer|TrustSet|n/a|
|5|Authorize|AccountSet|n/a|
|6|Unauthorize|AccountSet|n/a|
|8|RegularKey|AccountSet|n/a|
|9|NFTokenMinter|XLS20|n/a|
|10|EmitCallback|Hooks|n/a|
|16|HookAccount|Hooks|n/a|


## STOBJECT
Type 14

|Field Code|Field Name|Used by|Reserved by|
|-|-|-|-|
|1|ObjectEndMarker|Objects|n/a|
|2|TransactionMetaData|Metadata|n/a|
|3|CreatedNode|Metadata|n/a|
|4|DeletedNode|Metadata|n/a|
|5|ModifiedNode|Metadata|n/a|
|6|PreviousFields|Metadata|n/a|
|7|FinalFields|Metadata|n/a|
|8|NewFields|Metadata|n/a|
|9|TemplateEntry|unused/legacy|n/a|
|10|Memo|All Txn|n/a|
|11|SignerEntry|Multisign|n/a|
|12|NFToken|XLS20|n/a|
|13|EmitDetails|Hooks|n/a|
|14|Hook|Hooks|n/a|
|16|Signer|Multisign|n/a|
|18|Majority|Consensus|n/a|
|19|DisabledValidator|negativeUNL|n/a|
|20|EmittedTxn|Hooks|n/a|
|21|HookExecution|Hooks|n/a|
|22|HookDefinition|Hooks|n/a|
|23|HookParameter|Hooks|n/a|
|24|HookGrant|Hooks|n/a|


## STARRAY
Type 15

|Field Code|Field Name|Used by|Reserved by|
|-|-|-|-|
|1|ArrayEndMarker|Arrays|n/a|
|3|Signers|Multisign|n/a|
|4|SignerEntries|Multisign|n/a|
|5|Template|Templating|n/a|
|6|Necessary|legacy/unused|n/a|
|7|Sufficient|legacy/unused|n/a|
|8|AffectedNodes|Metadata|n/a|
|9|Memos|All Txn|n/a|
|10|NFTokens|XLS20|n/a|
|11|Hooks|Hooks|n/a|
|16|Majorities|Consensus|n/a|
|17|DisabledValidators|negativeUNL|n/a|
|18|HookExecutions|Hooks|n/a|
|19|HookParameters|Hooks|n/a|
|20|HookGrants|Hooks|n/a|


## UINT8
Type 16

|Field Code|Field Name|Used by|Reserved by|
|-|-|-|-|
|1|CloseResolution|Consensus|n/a|
|2|Method|legacy/unused|n/a|
|3|TransactionResult|Metadata|n/a|
|16|TickSize|Orderbooks|n/a|
|17|UNLModifyDisabling|negativeUNL|n/a|
|18|HookResult|Hooks|n/a|


## HASH160
Type 17

|Field Code|Field Name|Used by|Reserved by|
|-|-|-|-|
|1|TakerPaysCurrency|Offer|n/a|
|2|TakerPaysIssuer|Offer|n/a|
|3|TakerGetsCurrency|Offer|n/a|
|4|TakerGetsIssuer|Offer|n/a|


## PATHSET
Type 18

|Field Code|Field Name|Used by|Reserved by|
|-|-|-|-|
|1|Paths|Pathing|n/a|


## VECTOR256
Type 19

|Field Code|Field Name|Used by|Reserved by|
|-|-|-|-|
|1|Indexes|Ledger|n/a|
|2|Hashes|Ledger|n/a|
|3|Amendments|Ledger|n/a|
|4|NFTokenOffers|XLS20|n/a|


## UINT96
Type 20

|Field Code|Field Name|Used by|Reserved by|
|-|-|-|-|


## UINT192
Type 21

|Field Code|Field Name|Used by|Reserved by|
|-|-|-|-|


## UINT384
Type 22

|Field Code|Field Name|Used by|Reserved by|
|-|-|-|-|


## UINT512
Type 23

|Field Code|Field Name|Used by|Reserved by|
|-|-|-|-|


## TRANSACTION RESULTS


|Response Code|Response Name|Used by|Reserved by|
|-|-|-|-|
|-399|telLOCAL_ERROR|v1.10.0|n/a|
|-398|telBAD_DOMAIN|v1.10.0|n/a|
|-397|telBAD_PATH_COUNT|v1.10.0|n/a|
|-396|telBAD_PUBLIC_KEY|v1.10.0|n/a|
|-395|telFAILED_PROCESSING|v1.10.0|n/a|
|-394|telINSUF_FEE_P|v1.10.0|n/a|
|-393|telNO_DST_PARTIAL|v1.10.0|n/a|
|-392|telCAN_NOT_QUEUE|v1.10.0|n/a|
|-391|telCAN_NOT_QUEUE_BALANCE|v1.10.0|n/a|
|-390|telCAN_NOT_QUEUE_BLOCKS|v1.10.0|n/a|
|-389|telCAN_NOT_QUEUE_BLOCKED|v1.10.0|n/a|
|-388|telCAN_NOT_QUEUE_FEE|v1.10.0|n/a|
|-387|telCAN_NOT_QUEUE_FULL|v1.10.0|n/a|
|-299|temMALFORMED|v1.10.0|n/a|
|-298|temBAD_AMOUNT|v1.10.0|n/a|
|-297|temBAD_CURRENCY|v1.10.0|n/a|
|-296|temBAD_EXPIRATION|v1.10.0|n/a|
|-295|temBAD_FEE|v1.10.0|n/a|
|-294|temBAD_ISSUER|v1.10.0|n/a|
|-293|temBAD_LIMIT|v1.10.0|n/a|
|-292|temBAD_OFFER|v1.10.0|n/a|
|-291|temBAD_PATH|v1.10.0|n/a|
|-290|temBAD_PATH_LOOP|v1.10.0|n/a|
|-289|temBAD_REGKEY|v1.10.0|n/a|
|-288|temBAD_SEND_XRP_LIMIT|v1.10.0|n/a|
|-287|temBAD_SEND_XRP_MAX|v1.10.0|n/a|
|-286|temBAD_SEND_XRP_NO_DIRECT|v1.10.0|n/a|
|-285|temBAD_SEND_XRP_PARTIAL|v1.10.0|n/a|
|-284|temBAD_SEND_XRP_PATHS|v1.10.0|n/a|
|-283|temBAD_SEQUENCE|v1.10.0|n/a|
|-282|temBAD_SIGNATURE|v1.10.0|n/a|
|-281|temBAD_SRC_ACCOUNT|v1.10.0|n/a|
|-280|temBAD_TRANSFER_RATE|v1.10.0|n/a|
|-279|temDST_IS_SRC|v1.10.0|n/a|
|-278|temDST_NEEDED|v1.10.0|n/a|
|-277|temINVALID|v1.10.0|n/a|
|-276|temINVALID_FLAG|v1.10.0|n/a|
|-275|temREDUNDANT|v1.10.0|n/a|
|-274|temRIPPLE_EMPTY|v1.10.0|n/a|
|-273|temDISABLED|v1.10.0|n/a|
|-272|temBAD_SIGNER|v1.10.0|n/a|
|-271|temBAD_QUORUM|v1.10.0|n/a|
|-270|temBAD_WEIGHT|v1.10.0|n/a|
|-269|temBAD_TICK_SIZE|v1.10.0|n/a|
|-268|temINVALID_ACCOUNT_ID|v1.10.0|n/a|
|-267|temCANNOT_PREAUTH_SELF|v1.10.0|n/a|
|-266|temINVALID_COUNT|v1.10.0|n/a|
|-265|temUNCERTAIN|v1.10.0|n/a|
|-264|temUNKNOWN|v1.10.0|n/a|
|-263|temSEQ_AND_TICKET|v1.10.0|n/a|
|-262|temBAD_NFTOKEN_TRANSFER_FEE|v1.10.0|n/a|
|-199|tefFAILURE|v1.10.0|n/a|
|-198|tefALREADY|v1.10.0|n/a|
|-197|tefBAD_ADD_AUTH|v1.10.0|n/a|
|-196|tefBAD_AUTH|v1.10.0|n/a|
|-195|tefBAD_LEDGER|v1.10.0|n/a|
|-194|tefCREATED|v1.10.0|n/a|
|-193|tefEXCEPTION|v1.10.0|n/a|
|-192|tefINTERNAL|v1.10.0|n/a|
|-191|tefNO_AUTH_REQUIRED|v1.10.0|n/a|
|-190|tefPAST_SEQ|v1.10.0|n/a|
|-189|tefWRONG_PRIOR|v1.10.0|n/a|
|-188|tefMASTER_DISABLED|v1.10.0|n/a|
|-187|tefMAX_LEDGER|v1.10.0|n/a|
|-186|tefBAD_SIGNATURE|v1.10.0|n/a|
|-185|tefBAD_QUORUM|v1.10.0|n/a|
|-184|tefNOT_MULTI_SIGNING|v1.10.0|n/a|
|-183|tefBAD_AUTH_MASTER|v1.10.0|n/a|
|-182|tefINVARIANT_FAILED|v1.10.0|n/a|
|-181|tefTOO_BIG|v1.10.0|n/a|
|-180|tefNO_TICKET|v1.10.0|n/a|
|-179|tefNFTOKEN_IS_NOT_TRANSFERABLE|v1.10.0|n/a|
|-99|terRETRY|v1.10.0|n/a|
|-98|terFUNDS_SPENT|v1.10.0|n/a|
|-97|terINSUF_FEE_B|v1.10.0|n/a|
|-96|terNO_ACCOUNT|v1.10.0|n/a|
|-95|terNO_AUTH|v1.10.0|n/a|
|-94|terNO_LINE|v1.10.0|n/a|
|-93|terOWNERS|v1.10.0|n/a|
|-92|terPRE_SEQ|v1.10.0|n/a|
|-91|terLAST|v1.10.0|n/a|
|-90|terNO_RIPPLE|v1.10.0|n/a|
|-89|terQUEUED|v1.10.0|n/a|
|-88|terPRE_TICKET|v1.10.0|n/a|
|0|tesSUCCESS|v1.10.0|n/a|
|100|tecCLAIM|v1.10.0|n/a|
|101|tecPATH_PARTIAL|v1.10.0|n/a|
|102|tecUNFUNDED_ADD|v1.10.0|n/a|
|103|tecUNFUNDED_OFFER|v1.10.0|n/a|
|104|tecUNFUNDED_PAYMENT|v1.10.0|n/a|
|105|tecFAILED_PROCESSING|v1.10.0|n/a|
|121|tecDIR_FULL|v1.10.0|n/a|
|122|tecINSUF_RESERVE_LINE|v1.10.0|n/a|
|123|tecINSUF_RESERVE_OFFER|v1.10.0|n/a|
|124|tecNO_DST|v1.10.0|n/a|
|125|tecNO_DST_INSUF_XRP|v1.10.0|n/a|
|126|tecNO_LINE_INSUF_RESERVE|v1.10.0|n/a|
|127|tecNO_LINE_REDUNDANT|v1.10.0|n/a|
|128|tecPATH_DRY|v1.10.0|n/a|
|129|tecUNFUNDED|v1.10.0|n/a|
|130|tecNO_ALTERNATIVE_KEY|v1.10.0|n/a|
|131|tecNO_REGULAR_KEY|v1.10.0|n/a|
|132|tecOWNERS|v1.10.0|n/a|
|133|tecNO_ISSUER|v1.10.0|n/a|
|134|tecNO_AUTH|v1.10.0|n/a|
|135|tecNO_LINE|v1.10.0|n/a|
|136|tecINSUFF_FEE|v1.10.0|n/a|
|137|tecFROZEN|v1.10.0|n/a|
|138|tecNO_TARGET|v1.10.0|n/a|
|139|tecNO_PERMISSION|v1.10.0|n/a|
|140|tecNO_ENTRY|v1.10.0|n/a|
|141|tecINSUFFICIENT_RESERVE|v1.10.0|n/a|
|142|tecNEED_MASTER_KEY|v1.10.0|n/a|
|143|tecDST_TAG_NEEDED|v1.10.0|n/a|
|144|tecINTERNAL|v1.10.0|n/a|
|145|tecOVERSIZE|v1.10.0|n/a|
|146|tecCRYPTOCONDITION_ERROR|v1.10.0|n/a|
|147|tecINVARIANT_FAILED|v1.10.0|n/a|
|148|tecEXPIRED|v1.10.0|n/a|
|149|tecDUPLICATE|v1.10.0|n/a|
|150|tecKILLED|v1.10.0|n/a|
|151|tecHAS_OBLIGATIONS|v1.10.0|n/a|
|152|tecTOO_SOON|v1.10.0|n/a|
|153|tecHOOK_ERROR|v1.10.0|n/a|
|154|tecMAX_SEQUENCE_REACHED|v1.10.0|n/a|
|155|tecNO_SUITABLE_NFTOKEN_PAGE|v1.10.0|n/a|
|156|tecNFTOKEN_BUY_SELL_MISMATCH|v1.10.0|n/a|
|157|tecNFTOKEN_OFFER_TYPE_MISMATCH|v1.10.0|n/a|
|158|tecCANT_ACCEPT_OWN_NFTOKEN_OFFER|v1.10.0|n/a|
|159|tecINSUFFICIENT_FUNDS|v1.10.0|n/a|
|160|tecOBJECT_NOT_FOUND|v1.10.0|n/a|
|161|tecINSUFFICIENT_PAYMENT|v1.10.0|n/a|


