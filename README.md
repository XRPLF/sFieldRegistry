# SFCode Registry Tables
## How to use
1. If you are working on an Amendment to the XRP Ledger (or a sidechain) and you need additional serialized fields then you should register them here to avoid clobbering others.
2. Register by opening a PR against this repo with your proposed registration as changes to the tables below. Provided the reservations are reasonable these will be accepted. If your code is already in use then enter it into the `used by` column otherwise use the `reserved by` column.
3. Be descriptive but terse in the `reserved by` field. Other developers should understand why this code is being reserved.


## UINT8
Type 16

|Field Code|Field Name|Used by|Reserved by|
|-|-|-|-|
|1|CloseResolution|Consensus|n/a|
|2|Method|legacy/unused|n/a|
|3|TransactionResult|Metadata|n/a|
|16|TickSize|Orderbooks|n/a|
|17|UNLModifyDisabling|negativeUNL|n/a|


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

## UINT128
Type 4

|Field Code|Field Name|Used by|Reserved by|
|-|-|-|-|
|1|EmailHash|AccountSet|n/a|

## UINT160
Type 17

|Field Code|Field Name|Used by|Reserved by|
|-|-|-|-|
|1|TakerPaysCurrency|Offer|n/a|
|2|TakerPaysIssuer|Offer|n/a|
|3|TakerGetsCurrency|Offer|n/a|
|4|TakerGetsIssuer|Offer|n/a|

## UINT256
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
|20|HookCallbackFee|Hooks|n/a|
|21|LockedBalance|PaychanAndEscrowForTokens|n/a|
|22|BaseFeeDrops|FeeSettings|n/a|
|23|ReserveBaseDrops|FeeSettings|n/a|
|24|ReserveIncrementDrops|FeeSettings|n/a|

## VL
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

## Account Fields
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

## VECTOR256
Type 5

|Field Code|Field Name|Used by|Reserved by|
|-|-|-|-|
|1|Indexes|Ledger|n/a|
|2|Hashes|Ledger|n/a|
|3|Amendments|Ledger|n/a|
|4|NFTokenOffers|XLS20|n/a|

## PATHSET
Type 18

|Field Code|Field Name|Used by|Reserved by|
|-|-|-|-|
|1|Paths|Pathing|n/a|

## OBJECT
Type 14

|Field Code|Field Name|Used by|Reserved by|
|-|-|-|-|
|1|<EndOfObject>|Objects|n/a|
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

## ARRAY
Type 15

|Field Code|Field Name|Used by|Reserved by|
|-|-|-|-|
|1|<EndOfArray>|Arrays|n/a|
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
